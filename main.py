#!/usr/bin/env python3
"""One-line review of the most boring everyday object.

Writes the review to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
with no trailing newline, and prints it to stdout.

Entry for make.fun's "The Most Boring Object, Reviewed in One Line".
Python 3 standard library only; deterministic; no network.
"""

import os

LINE = (
    "The bag of plastic bags under my sink has outlived three kitchens, "
    "two relationships and one flood, and not one of them has ever been used."
)

# Self-check: the competition gate requires 1-200 chars, a single line,
# no trailing newline. Fail loudly here instead of shipping a bad entry.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
