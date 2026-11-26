#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes one line to /output/entry.txt: the text a gamer sends the boss
to skip work on GTA 6 launch week. One line, plain words, no setup,
no explanation, no signature — the way a hurried text actually reads.

The line is a fixed string: deterministic, byte-identical on every run.
"""

import os

ENTRY = "Have to wait in for a delivery, they gave a nine to five window and someone has to sign."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
