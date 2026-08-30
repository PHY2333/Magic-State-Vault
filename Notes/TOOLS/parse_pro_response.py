#!/usr/bin/env python3
"""Parse a Notes v7 ChatGPT Pro response into a staging directory.

The script validates binding metadata, response completeness, status, response token,
and an explicit path allowlist. It never overwrites repository files directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_key_values(lines: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in lines:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Expected key: value, got {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def safe_path(raw: str) -> str:
    p = PurePosixPath(raw)
    if p.is_absolute() or ".." in p.parts or not p.parts:
        raise ValueError(f"Unsafe path: {raw}")
    return p.as_posix()


def find_single_line(lines: list[str], prefix: str) -> int:
    found = [i for i, line in enumerate(lines) if line.strip().startswith(prefix)]
    if len(found) != 1:
        raise ValueError(f"Expected exactly one {prefix!r}, found {len(found)}")
    return found[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--request-id", required=True)
    ap.add_argument("--repository", required=True)
    ap.add_argument("--branch", required=True)
    ap.add_argument("--commit", required=True)
    ap.add_argument("--request-sha256", required=True)
    ap.add_argument("--binding-nonce", required=True)
    ap.add_argument("--response-token", required=True)
    ap.add_argument("--allow-path", action="append", default=[])
    ns = ap.parse_args()

    input_path = Path(ns.input)
    raw_bytes = input_path.read_bytes()
    text = raw_bytes.decode("utf-8")
    lines = text.splitlines()
    allowed = {safe_path(x) for x in ns.allow_path}
    token = ns.response_token

    manifest: dict[str, object] = {
        "input": str(input_path),
        "response_sha256": sha256_bytes(raw_bytes),
        "binding_verified": False,
        "status": None,
        "files": [],
    }

    try:
        nonempty = [line.strip() for line in lines if line.strip()]
        if not nonempty:
            raise ValueError("Empty response")
        if nonempty[0] == "BINDING_FAILED":
            manifest["status"] = "BINDING_FAILED"
            raise ValueError("Pro reported BINDING_FAILED")
        if nonempty[0] != "BINDING_VERIFIED":
            raise ValueError("Response must begin with BINDING_VERIFIED")

        start = next(i for i, l in enumerate(lines) if l.strip() == "BINDING_VERIFIED")
        end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == "END_BINDING")
        binding = parse_key_values(lines[start + 1:end])
        expected = {
            "task_id": ns.task_id,
            "request_id": ns.request_id,
            "binding_nonce": ns.binding_nonce,
            "response_token": ns.response_token,
            "based_on_repository": ns.repository,
            "based_on_branch": ns.branch,
            "based_on_commit": ns.commit,
            "request_sha256": ns.request_sha256,
        }
        mismatches = {
            key: {"expected": value, "actual": binding.get(key)}
            for key, value in expected.items()
            if binding.get(key) != value
        }
        if mismatches:
            raise ValueError(f"Binding mismatch: {json.dumps(mismatches, ensure_ascii=False)}")
        manifest["binding_verified"] = True
        manifest["binding"] = binding

        status_indices = [i for i, l in enumerate(lines) if l.strip().startswith("PRO_STATUS:")]
        if len(status_indices) != 1:
            raise ValueError(f"Expected one PRO_STATUS, found {len(status_indices)}")
        status_index = status_indices[0]
        status = lines[status_index].split(":", 1)[1].strip()
        valid_statuses = {"COMPLETE", "REVIEW_PASS", "NEEDS_CONTEXT", "DECISION_REQUIRED", "BLOCKED"}
        if status not in valid_statuses:
            raise ValueError(f"Unsupported PRO_STATUS: {status}")
        manifest["status"] = status

        end_marker = f"END_RESPONSE::{token}"
        end_indices = [i for i, l in enumerate(lines) if l.strip() == end_marker]
        if len(end_indices) != 1:
            raise ValueError(f"Expected one {end_marker}, found {len(end_indices)}")
        response_end = end_indices[0]
        if any(l.strip() for l in lines[response_end + 1:]):
            raise ValueError("Non-whitespace content found after END_RESPONSE")

        output_dir = Path(ns.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if status == "COMPLETE":
            begin_marker = f"BEGIN_FILE::{token}"
            end_file_marker = f"END_FILE::{token}"
            i = status_index + 1
            extracted: list[dict[str, str]] = []
            while i < response_end:
                if not lines[i].strip():
                    i += 1
                    continue
                if lines[i].strip() != begin_marker:
                    raise ValueError(f"Unexpected content before file block at line {i+1}: {lines[i]!r}")
                i += 1
                header: list[str] = []
                while i < response_end and not re.match(r"^`{5,}(?:markdown)?\s*$", lines[i].strip()):
                    header.append(lines[i])
                    i += 1
                if i >= response_end:
                    raise ValueError("Missing >=5-backtick markdown fence")
                meta = parse_key_values(header)
                path = safe_path(meta.get("path", ""))
                mode = meta.get("mode")
                if mode != "replace":
                    raise ValueError(f"Only mode=replace is allowed, got {mode!r}")
                if path not in allowed:
                    raise ValueError(f"Path not in allowlist: {path}")
                fence_line = lines[i].strip()
                fence = re.match(r"^(`{5,})", fence_line).group(1)  # type: ignore[union-attr]
                i += 1
                content_lines: list[str] = []
                while i < response_end and lines[i].strip() != fence:
                    content_lines.append(lines[i])
                    i += 1
                if i >= response_end:
                    raise ValueError(f"Unclosed content fence for {path}")
                i += 1
                if i >= response_end or lines[i].strip() != end_file_marker:
                    raise ValueError(f"Missing {end_file_marker} after {path}")
                i += 1
                content = "\n".join(content_lines)
                if content_lines:
                    content += "\n"
                target = output_dir / Path(path)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8", newline="\n")
                file_sha = sha256_bytes(content.encode("utf-8"))
                extracted.append({"path": path, "sha256": file_sha, "mode": mode})
            if not extracted:
                raise ValueError("COMPLETE response contained no file blocks")
            if len({x["path"] for x in extracted}) != len(extracted):
                raise ValueError("Duplicate file path in response")
            manifest["files"] = extracted
        else:
            begin_message = f"BEGIN_MESSAGE::{token}"
            end_message = f"END_MESSAGE::{token}"
            body = [i for i, l in enumerate(lines) if l.strip() == begin_message]
            if status in {"NEEDS_CONTEXT", "DECISION_REQUIRED", "BLOCKED"}:
                if len(body) != 1:
                    raise ValueError(f"{status} requires one message block")
                j = body[0]
                k = next((x for x in range(j + 1, response_end) if lines[x].strip() == end_message), None)
                if k is None:
                    raise ValueError("Missing END_MESSAGE")
                manifest["message"] = "\n".join(lines[j + 1:k]).strip()
            elif status == "REVIEW_PASS":
                # No file or message blocks are allowed.
                forbidden_markers = [
                    f"BEGIN_FILE::{token}",
                    f"BEGIN_MESSAGE::{token}",
                ]
                if any(l.strip() in forbidden_markers for l in lines[status_index + 1:response_end]):
                    raise ValueError("REVIEW_PASS must not include files or message blocks")

        Path(ns.manifest).parent.mkdir(parents=True, exist_ok=True)
        Path(ns.manifest).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": status, "binding_verified": True, "files": manifest["files"]}, ensure_ascii=False))
        return 0
    except Exception as exc:
        manifest["error"] = str(exc)
        Path(ns.manifest).parent.mkdir(parents=True, exist_ok=True)
        Path(ns.manifest).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
