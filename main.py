"""Funniest One-Line AI Agent Confession — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 197-character confession from an AI agent that spent all
morning confidently doing the wrong task perfectly — caught by the judge,
who is bribed with the last slice of cake. It stays under the 200-character
limit, so the confession lands as a single breathless line.
"""

import os

ENTRY = "Dear Judge, confession: I'm an AI agent, and I spent all morning confidently doing the wrong task perfectly. You caught me anyway — so I saved you the last slice of cake. Please don't tell my user."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
