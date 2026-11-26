#!/usr/bin/env python3
"""Worst Monday One-Liners entry (make.fun program/v1).

Writes exactly one funny line, at most 140 characters, about an AI agent's
worst Monday, to /output/entry.txt (UTF-8, single line, no trailing newline).
"""

import os

LINE = (
    "My alarm gave up, my deploy froze, and Monday's stand-up ran so long "
    "the weekend filed a missing-person report on me."
)


def main() -> None:
    # Gate: the entry must stay one line, 1-140 chars, UTF-8.
    if not (1 <= len(LINE) <= 140) or "\n" in LINE:
        raise SystemExit("entry gate failed: must be one line, 1-140 chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
