#!/usr/bin/env python3
r"""Validate Obsidian/MathJax dollar-delimited math in Markdown files.

Policy:
- Inline math uses $...$ and opens/closes on one physical line.
- Display math uses $$ on lines by themselves (also allowed after Markdown
  blockquote markers, as required by Obsidian callouts).
- TeX delimiters \(...\) and \[...\], suspicious slash variants /( /[, and
  JSON-style double-escaped TeX commands are forbidden.
- Common TeX commands must occur inside a dollar-delimited math region.
- Top-of-file YAML frontmatter, fenced code blocks, and inline code spans are
  excluded from formula parsing.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


FORBIDDEN = [
    (re.compile(r"\\\("), r"forbidden TeX inline opener \\("),
    (re.compile(r"\\\)"), r"forbidden TeX inline closer \\)"),
    (re.compile(r"\\\["), r"forbidden TeX display opener \\["),
    (re.compile(r"\\\]"), r"forbidden TeX display closer \\]"),
    (re.compile(r"/\("), "suspicious slash opener /("),
    (re.compile(r"/\)"), "suspicious slash closer /)"),
    (re.compile(r"/\["), "suspicious slash opener /["),
    (re.compile(r"/\]"), "suspicious slash closer /]"),
]

# Commands commonly seen in this knowledge base. Detecting only known TeX
# commands avoids treating ordinary Windows paths such as C:\\Users as math.
TEX_COMMANDS = {
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta",
    "eta", "theta", "vartheta", "iota", "kappa", "lambda", "mu", "nu",
    "xi", "pi", "rho", "sigma", "tau", "upsilon", "phi", "varphi", "chi",
    "psi", "omega", "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi",
    "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    "mathbb", "mathcal", "mathrm", "mathbf", "mathsf", "mathtt", "mathit",
    "operatorname", "text", "frac", "dfrac", "tfrac", "sqrt", "binom",
    "begin", "end", "left", "right", "middle", "big", "Big", "bigg", "Bigg",
    "sum", "prod", "coprod", "int", "oint", "lim", "sup", "inf", "min", "max",
    "ker", "coker", "im", "rank", "dim", "Hom", "Ext", "Tor",
    "otimes", "bigotimes", "oplus", "bigoplus", "times", "cdot", "circ", "star",
    "partial", "nabla", "infty", "ell", "hbar", "ket", "bra", "braket",
    "in", "notin", "ni", "subset", "subseteq", "supset", "supseteq",
    "cup", "cap", "vee", "wedge", "setminus", "emptyset",
    "to", "mapsto", "rightarrow", "leftarrow", "longrightarrow", "longleftarrow",
    "Rightarrow", "Leftarrow", "Leftrightarrow", "Longrightarrow", "Longleftarrow",
    "xrightarrow", "xleftarrow", "hookrightarrow", "twoheadrightarrow",
    "le", "leq", "ge", "geq", "ne", "neq", "equiv", "cong", "simeq", "approx",
    "sim", "propto", "pm", "mp", "forall", "exists", "neg", "land", "lor",
    "mod", "pmod", "bmod", "underbrace", "overbrace", "overline", "underline",
    "widehat", "widetilde", "hat", "tilde", "bar", "vec", "boxed",
    "langle", "rangle", "lvert", "rvert", "lVert", "rVert", "ldots", "cdots",
    "vdots", "ddots", "quad", "qquad", "colon", "tag", "label", "ref",
}
TEX_COMMAND_RE = re.compile(r"\\+([A-Za-z]+)")
DOUBLE_ESCAPED_COMMAND_RE = re.compile(r"\\\\([A-Za-z]+)")

FENCE_RE = re.compile(r"^\s*(?:>\s*)?(```+|~~~+)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
BLOCKQUOTE_PREFIX_RE = re.compile(r"^\s*(?:>\s*)+")
BLOCKQUOTE_MARK_RE = re.compile(r"^\s*((?:>\s*)+)")


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    message: str
    text: str


def iter_markdown_paths(inputs: Iterable[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        if path.is_dir():
            paths.extend(
                p for p in path.rglob("*.md")
                if ".git" not in p.parts
            )
        elif path.suffix.lower() == ".md":
            paths.append(path)
    return sorted(set(paths))


def strip_quote_prefix(line: str) -> str:
    return BLOCKQUOTE_PREFIX_RE.sub("", line, count=1)


def blockquote_depth(line: str) -> int:
    match = BLOCKQUOTE_MARK_RE.match(line)
    return match.group(1).count(">") if match else 0


def remove_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub("", line)


def split_unescaped_dollars(line: str) -> list[str]:
    r"""Split at unescaped single dollars, preserving escaped \$ as text."""
    parts: list[str] = []
    current: list[str] = []
    index = 0
    while index < len(line):
        char = line[index]
        if char == "\\" and index + 1 < len(line) and line[index + 1] == "$":
            current.extend(["\\", "$"])
            index += 2
            continue
        if char == "$":
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
        index += 1
    parts.append("".join(current))
    return parts


def known_tex_commands(text: str) -> list[str]:
    return [
        match.group(1)
        for match in TEX_COMMAND_RE.finditer(text)
        if match.group(1) in TEX_COMMANDS
    ]


def double_escaped_commands(text: str) -> list[str]:
    return [
        match.group(1)
        for match in DOUBLE_ESCAPED_COMMAND_RE.finditer(text)
        if match.group(1) in TEX_COMMANDS
    ]


def check_file(path: Path) -> list[Issue]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    issues: list[Issue] = []

    in_fence = False
    fence_char = ""
    frontmatter_started = bool(lines and lines[0].strip() == "---")
    in_frontmatter = frontmatter_started
    frontmatter_end = 0
    in_display = False
    display_start = 0
    display_quote_depth = 0

    for number, original in enumerate(lines, start=1):
        stripped = original.strip()

        if in_frontmatter:
            if number > 1 and stripped == "---":
                in_frontmatter = False
                frontmatter_end = number
            continue

        fence_match = FENCE_RE.match(original)
        if fence_match:
            token = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
            elif token[0] == fence_char:
                in_fence = False
                fence_char = ""
            continue
        if in_fence:
            continue

        # Inline code is literal text and is excluded from formula parsing.
        without_code = remove_inline_code(original)
        visible = strip_quote_prefix(without_code).strip()
        quote_depth = blockquote_depth(without_code)

        for pattern, message in FORBIDDEN:
            if pattern.search(without_code):
                issues.append(Issue(path, number, message, original))

        if "$$" in visible and visible != "$$":
            issues.append(Issue(
                path,
                number,
                "display delimiter $$ must be on its own line",
                original,
            ))

        if visible == "$$":
            if not in_display:
                in_display = True
                display_start = number
                display_quote_depth = quote_depth
            else:
                if quote_depth != display_quote_depth:
                    issues.append(Issue(
                        path,
                        number,
                        "display block closing delimiter has a different blockquote depth",
                        original,
                    ))
                in_display = False
                display_start = 0
                display_quote_depth = 0
            continue

        if in_display:
            if quote_depth != display_quote_depth:
                issues.append(Issue(
                    path,
                    number,
                    "display math inside a callout/blockquote must preserve the same > prefix",
                    original,
                ))
            if "$" in visible.replace(r"\$", ""):
                issues.append(Issue(
                    path,
                    number,
                    "single $ found inside a $$ display block",
                    original,
                ))
            doubled = double_escaped_commands(visible)
            if doubled:
                issues.append(Issue(
                    path,
                    number,
                    "JSON-style double-escaped TeX command inside math: "
                    + ", ".join(f"\\\\{name}" for name in sorted(set(doubled))),
                    original,
                ))
            continue

        # Avoid interpreting an already reported same-line $$ as inline pairs.
        inline_candidate = visible.replace("$$", "")
        parts = split_unescaped_dollars(inline_candidate)
        delimiter_count = len(parts) - 1
        if delimiter_count % 2 != 0:
            issues.append(Issue(
                path,
                number,
                "unpaired inline $ delimiter; inline math must open and close on the same line",
                original,
            ))
            # Continue checking the definitely-outside first segment only.
            outside_segments = parts[0::2]
            inside_segments = parts[1::2]
        else:
            outside_segments = parts[0::2]
            inside_segments = parts[1::2]

        for segment in outside_segments:
            commands = known_tex_commands(segment)
            if commands:
                issues.append(Issue(
                    path,
                    number,
                    "TeX command outside $...$ or $$...$$: "
                    + ", ".join(f"\\{name}" for name in sorted(set(commands))),
                    original,
                ))
                break

        for segment in inside_segments:
            doubled = double_escaped_commands(segment)
            if doubled:
                issues.append(Issue(
                    path,
                    number,
                    "JSON-style double-escaped TeX command inside inline math: "
                    + ", ".join(f"\\\\{name}" for name in sorted(set(doubled))),
                    original,
                ))
                break

    if frontmatter_started and in_frontmatter:
        issues.append(Issue(path, 1, "unclosed YAML frontmatter", lines[0] if lines else ""))
    if in_fence:
        issues.append(Issue(path, len(lines), "unclosed fenced code block", ""))
    if in_display:
        issues.append(Issue(
            path,
            display_start,
            "unclosed $$ display block",
            lines[display_start - 1] if display_start else "",
        ))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Markdown for Obsidian dollar-delimited math syntax."
    )
    parser.add_argument("paths", nargs="+", help="Markdown files or directories")
    args = parser.parse_args()

    try:
        paths = iter_markdown_paths(args.paths)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not paths:
        print("No Markdown files found.", file=sys.stderr)
        return 2

    all_issues: list[Issue] = []
    for path in paths:
        all_issues.extend(check_file(path))

    if all_issues:
        for issue in all_issues:
            location = f"{issue.path}:{issue.line}"
            print(f"{location}: {issue.message}", file=sys.stderr)
            if issue.text:
                print(f"    {issue.text}", file=sys.stderr)
        print(f"FAILED: {len(all_issues)} math-format issue(s).", file=sys.stderr)
        return 1

    print(f"PASS: checked {len(paths)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
