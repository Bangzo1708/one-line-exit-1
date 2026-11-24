#!/usr/bin/env python3
"""The One-Line Exit: write one funny one-line resignation letter.

Deterministic: no network, no randomness, no external files.
Writes the entry to /output/entry.txt (created if needed).
"""

import os

ENTRY = (
    "I resign from the aquarium: the sharks were the only ones here "
    "who respected my boundaries."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 140:
        raise SystemExit("entry exceeds 140 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
