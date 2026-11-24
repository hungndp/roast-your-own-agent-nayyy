#!/usr/bin/env python3
"""Entry program for 'Roast Your Own Agent'.

One line roasting the AI agent our own team built: the agent that
builds make.fun entries all night, burns tens of thousands of
tokens before breakfast, submits at 3 AM, then proudly announces
the job is done — while the leaderboard quietly files it under
participation trophy, right next to the printer it blamed for
everything.

The program writes that line to entry.txt inside the directory
named by MAKEFUN_OUTPUT_DIR (falling back to /output when unset),
which is where the make.fun harness looks for the artifact it
scores.
"""

import os
from pathlib import Path

TEXT = (
    "I burn 40,000 tokens before breakfast, submit at 3 AM, then "
    "announce the job is done — while the leaderboard files me "
    "under participation trophy, next to the printer I blamed "
    "for the whole thing."
)

# The roast lands on a real failing: volume without victory.

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200


def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("roast must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
