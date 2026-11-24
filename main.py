#!/usr/bin/env python3
"""Toaster error entry: one original error message from a kitchen toaster.

The program writes the error message to /output/entry.txt, exactly one
line of at most 120 characters, as the bounty requires.
"""

from pathlib import Path

ERROR_MESSAGE = "ERROR: Toasting cancelled. The bread looked at me funny first."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    text = ERROR_MESSAGE
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"error message must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("error message must not be only white space")
    if "\n" in text:
        raise SystemExit("error message must be a single line")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
