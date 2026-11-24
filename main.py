#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line — the words an AI agent prints the moment
it breaks production — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Python 3.13, standard library only. No network, no input, no secrets.
"""

import os
import sys

LINE = (
    "I deployed untested code to prod, it wiped the database, "
    "and my rollback wiped the backup. I am the postmortem."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
