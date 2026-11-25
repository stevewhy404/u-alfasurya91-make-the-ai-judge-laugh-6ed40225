#!/usr/bin/env python3
"""Make the AI Judge Laugh — one line about office life.

Writes a single office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-200 characters, one line, not whitespace-only.
"""
import os

LINE = "The printer only jams when the document is urgent, which is how I know it understands my deadlines better than my manager does."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
