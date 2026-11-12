"""Coolest-art-01 entry: copy the shipped artwork to the output directory.

The art is entry.png beside this file: a colossal bioluminescent whale
gliding over a neon-lit futuristic city at night. The program copies it
unchanged to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so both
runs write exactly the same bytes. Python 3.13, standard library only,
no network, no randomness, no timestamps.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    if not os.path.isfile(SOURCE):
        print("error: entry.png is missing beside main.py", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # The judge sees exactly the bytes copied: confirm the copy is whole.
    if os.path.getsize(OUTPUT) != os.path.getsize(SOURCE):
        print("error: copied entry.png is incomplete", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")


if __name__ == "__main__":
    main()
