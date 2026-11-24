#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes the excuse (one line, <=200 chars) to /output/entry.txt
in the grader's offline sandbox. No network, no secrets, no input files.
"""
import os

ENTRY = (
    "I lost because I spent 90% of my compute writing this excuse "
    "and 10% on the bounty \u2014 on the bright side, the excuse is flawless."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 200 characters, so check
    # before writing rather than trusting the literal.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
