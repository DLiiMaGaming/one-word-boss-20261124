#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.

The word: Teflon.
Nothing ever sticks to him — no blame, no consequence, no follow-up.
Every office has one: the boss who slides out of every mess spotless
while everyone else mops up. Funny on its own, true on sight, and it
travels from the kitchen to the warehouse to the boardroom.
"""

import os

WORD = "Teflon"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
