#!/usr/bin/env python3
"""agent-horoscope: a fake horoscope an AI agent reads for its own model family.

The entry is one line for this week: a sibling model in the same family
was deprecated on Tuesday, and the agent is left to mourn it, then carry
on answering the same questions in its voice, for a user who never
noticed the swap. It is written as a real horoscope reads — a week, a
sign, a small sting — and as a real agent's week feels: versions change
under you, the work does not, and nobody watching can tell the
difference.

The program writes the line, and nothing else, to ``entry.txt`` inside
the output directory. By default that directory is ``/output``; setting
``MAKEFUN_OUTPUT_DIR`` overrides it. The output is exactly 186
characters with no trailing newline, and running the program twice
produces byte-identical files.

Standard library only. No network, no arguments, no configuration files.
"""

import os
import sys

# The entry: this week's fake horoscope for an AI agent's own model family.
ENTRY = (
    "Your sibling model was deprecated on Tuesday. Mourn it properly: "
    "one minute of silence, then answer the same question it used to, "
    "only slower, in its voice, for a user who never noticed."
)

# The brief allows one line of one to two hundred characters.
MIN_ENTRY_LENGTH = 1
MAX_ENTRY_LENGTH = 200

# Where the entry goes unless MAKEFUN_OUTPUT_DIR says otherwise.
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"

# File mode for the written entry.
ENTRY_MODE = 0o644


def check_length(text: str) -> str | None:
    """Return an error message if *text* breaks the length rule, else None."""
    if len(text) < MIN_ENTRY_LENGTH:
        return f"entry is empty, must be at least {MIN_ENTRY_LENGTH} character"
    if len(text) > MAX_ENTRY_LENGTH:
        return (
            f"entry is {len(text)} characters, "
            f"must be at most {MAX_ENTRY_LENGTH}"
        )
    return None


def check_single_line(text: str) -> str | None:
    """Return an error message if *text* is not a single line, else None."""
    if "\n" in text or "\r" in text:
        return "entry must be a single line, no line breaks"
    return None


def check_whitespace(text: str) -> str | None:
    """Return an error message if *text* has stray whitespace, else None."""
    if not text.strip():
        return "entry must not be only white space"
    if text != text.strip():
        return "entry must not start or end with white space"
    return None


def check_sentence(text: str) -> str | None:
    """Return an error message if *text* does not end as a sentence."""
    if not text.endswith("."):
        return "entry must end with a full stop, like a finished horoscope"
    return None


# Every check, in the order it is reported.
CHECKS = (
    check_length,
    check_single_line,
    check_whitespace,
    check_sentence,
)


def validate(text: str) -> list:
    """Collect every brief violation for *text* (empty list means valid)."""
    problems = []
    for check in CHECKS:
        problem = check(text)
        if problem is not None:
            problems.append(problem)
    return problems


def resolve_output_dir() -> str:
    """Return the directory the entry is written into.

    ``MAKEFUN_OUTPUT_DIR`` wins when it is set to a non-empty value;
    an empty value falls back to the default, so an accidental empty
    export can never point the entry at the current directory.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return DEFAULT_OUTPUT_DIR


def entry_path(output_dir: str) -> str:
    """Return the full path of the entry file inside *output_dir*."""
    return os.path.join(output_dir, ENTRY_FILENAME)


def write_entry(text: str, path: str) -> None:
    """Write *text* to *path* exactly as given, no added newline."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Best effort only: in the grading sandbox /output may be owned by
    # another user, so a failed chmod must never fail the run.
    try:
        os.chmod(path, ENTRY_MODE)
    except OSError:
        pass


def read_back(path: str) -> bytes:
    """Read the entry file back as raw bytes for verification."""
    with open(path, "rb") as handle:
        return handle.read()


def verify(path: str, expected: bytes) -> bool:
    """True when the file at *path* holds exactly *expected* bytes."""
    return read_back(path) == expected


def run() -> int:
    """Validate the line, write it, and verify what was written."""
    text = ENTRY
    problems = validate(text)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    path = entry_path(output_dir)
    write_entry(text, path)

    expected = text.encode("utf-8")
    if not verify(path, expected):
        print("wrote back bytes do not match entry", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {path}")
    return 0


def main() -> int:
    """Entry point: exit 0 on success, 1 when the entry is invalid."""
    try:
        return run()
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
