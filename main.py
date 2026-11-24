#!/usr/bin/env python3
"""One-line office joke entry for 'Make the AI Judge Laugh: Office Jokes'
(make.fun).

Prints a single joke line about office life and nothing else. Model-free
and fully deterministic: the same line, byte for byte, on every run.
No wall clock, no randomness, no network, no API keys.
"""

import sys

JOKE = (
    "The office printer only jams on urgent documents, which is how I "
    "learned it has a better sense of deadlines than my manager."
)


def main(argv):
    """Print the joke; --help / -h prints usage instead."""
    if "--help" in argv or "-h" in argv:
        print("Usage: python3 main.py [--help]")
        print("Prints a one-line office joke for make.fun.")
        return 0
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
