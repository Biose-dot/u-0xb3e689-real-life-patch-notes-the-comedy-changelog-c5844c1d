#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

A release note for a bug in human biology: humans require 8 hours of sleep to function. Fixed in v2.4.1 — sleep now optional.
"""
import os

ENTRY = 'v2.4.1: Fixed bug where humans require 8 hours of sleep to function. Sleep now optional. Side effect: nobody knows what day it is.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
