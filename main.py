#!/usr/bin/env python3
"""Ship It Friday — writes one funny git commit message to /output/entry.txt.

The commit message is the funniest line an AI coding agent writes in the
moment before it breaks production on a Friday: cheerfully confident,
completely unaware of the disaster it is about to cause.
"""

import os

ENTRY = "fix: drop the prod database, it looked unused — 99% confident, shipping Friday, see you Monday"
# One line, no trailing newline in the file: the gate counts characters,
# and a newline would add one without adding any joke.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
