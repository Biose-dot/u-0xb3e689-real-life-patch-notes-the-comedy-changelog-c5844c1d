#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

The patch moves from sleep to the 3 a.m. sneeze: quiet at last, with the classic release-note sting — the fix makes the hiccups louder.
"""
import os

ENTRY = 'v2.4.1: Fixed the bug where sneezing at 3 a.m. wakes the whole house. Sneezes are now quiet. Side effect: hiccups got louder.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
