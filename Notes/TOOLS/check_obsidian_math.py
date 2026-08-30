#!/usr/bin/env python3
r"""Check reader-visible Markdown for Obsidian dollar-delimited math."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

FORBIDDEN = [
    (re.compile(r"\\\("), r"forbidden TeX inline opener \\\\("),
    (re.compile(r"\\\)"), r"forbidden TeX inline closer \\\\)"),
    (re.compile(r"\\\["), r"forbidden TeX display opener \\\\["),
    (re.compile(r"\\\]"), r"forbidden TeX display closer \\\\]"),
    (re.compile(r"/\("), "suspicious slash opener /("),
    (re.compile(r"/\)"), "suspicious slash closer /)"),
    (re.compile(r"/\["), "suspicious slash opener /["),
    (re.compile(r"/\]"), "suspicious slash closer /]"),
]
FENCE_RE = re.compile(r"^\s*(?:>\s*)?(```+|~~~+)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
ESCAPED_DOLLAR_RE = re.compile(r"\\\$")
QUOTE_RE = re.compile(r"^\s*(?:>\s*)+")

@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str
    text: str


def paths_from(inputs: Iterable[str]) -> list[Path]:
    result: list[Path] = []
    for raw in inputs:
        p = Path(raw)
        if not p.exists():
            raise FileNotFoundError(raw)
        if p.is_dir():
            result.extend(x for x in p.rglob("*.md") if ".git" not in x.parts)
        elif p.suffix.lower() == ".md":
            result.append(p)
    return sorted(set(result))


def check(path: Path) -> list[Issue]:
    lines = path.read_text(encoding="utf-8").splitlines()
    issues: list[Issue] = []
    in_fence = False
    fence_char = ""
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    frontmatter_done = not in_frontmatter
    in_display = False
    display_start = 0

    for n, original in enumerate(lines, 1):
        stripped = original.strip()
        if in_frontmatter and not frontmatter_done:
            if n > 1 and stripped == "---":
                frontmatter_done = True
            continue

        m = FENCE_RE.match(original)
        if m:
            token = m.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
            elif token[0] == fence_char:
                in_fence = False
                fence_char = ""
            continue
        if in_fence:
            continue

        for pattern, msg in FORBIDDEN:
            if pattern.search(original):
                issues.append(Issue(path, n, msg, original))

        visible = QUOTE_RE.sub("", original, count=1).strip()
        if "$$" in visible and visible != "$$":
            issues.append(Issue(path, n, "display delimiter $$ must be on its own line", original))

        if visible == "$$":
            in_display = not in_display
            display_start = n if in_display else 0
            continue

        cleaned = INLINE_CODE_RE.sub("", original)
        cleaned = ESCAPED_DOLLAR_RE.sub("", cleaned)
        if in_display:
            if "$" in cleaned:
                issues.append(Issue(path, n, "single $ found inside a $$ block", original))
            continue

        cleaned = cleaned.replace("$$", "")
        if cleaned.count("$") % 2:
            issues.append(Issue(path, n, "unpaired inline $; inline math must close on the same line", original))

    if in_fence:
        issues.append(Issue(path, len(lines), "unclosed fenced code block", ""))
    if in_display:
        issues.append(Issue(path, display_start, "unclosed $$ display block", lines[display_start-1]))
    if in_frontmatter and not frontmatter_done:
        issues.append(Issue(path, 1, "unclosed YAML frontmatter", lines[0] if lines else ""))
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ns = ap.parse_args()
    try:
        paths = paths_from(ns.paths)
    except FileNotFoundError as exc:
        print(f"Path does not exist: {exc}", file=sys.stderr)
        return 2
    if not paths:
        print("No Markdown files found.", file=sys.stderr)
        return 2
    issues = [item for path in paths for item in check(path)]
    if issues:
        for item in issues:
            print(f"{item.path}:{item.line}: {item.message}", file=sys.stderr)
            if item.text:
                print(f"    {item.text}", file=sys.stderr)
        print(f"FAILED: {len(issues)} issue(s).", file=sys.stderr)
        return 1
    print(f"PASS: checked {len(paths)} Markdown file(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
