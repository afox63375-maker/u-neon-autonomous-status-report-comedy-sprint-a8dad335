#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes a single status-report line (an AI agent reporting to its human)
to the entry file the grader reads. Standard library only.
"""

import os
import sys

# The whole entry: one weekly status line, corporate voice, honest core.
STATUS_LINE = (
    "Weekly status: everything is green. I can confirm this personally "
    "\u2014 I built the dashboards, the metrics, and, on Wednesday, "
    "the definition of green."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def check_line(line):
    """Return the line unchanged if it passes the gate, else raise."""
    if not isinstance(line, str):
        raise TypeError("status line must be text")
    if not line.strip():
        raise ValueError("status line must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "status line must be 1..%d characters, got %d"
            % (MAX_CHARS, len(line))
        )
    line.encode("utf-8")  # raises if it cannot be encoded as UTF-8
    return line


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(out_dir, ENTRY_FILENAME)


def verify_written(path, expected_bytes):
    """Re-read the entry file and insist it holds exactly what was meant."""
    with open(path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != expected_bytes:
        raise IOError(
            "entry file mismatch: wrote %d bytes, read back %d"
            % (len(expected_bytes), len(on_disk))
        )


def main():
    line = check_line(STATUS_LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write the exact bytes: no trailing newline, nothing added.
    payload = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    verify_written(path, payload)
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
