#!/usr/bin/env python3
"""Entry for make.fun: Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt,
then reads it back to prove the file holds exactly the intended text.
"""

import hashlib
import os

ENTRY = "We insure houseplants against death, because millennials who kill every fern they own will pay to stop feeling like murderers."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file must hold exactly what we wrote.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "read-back mismatch"
    assert written.count(b"\n") == 0, "entry must be a single line"
    print("entry ok: %d bytes sha256=%s" % (len(written), hashlib.sha256(written).hexdigest()))


if __name__ == "__main__":
    main()
