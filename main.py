#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single line (1-200 characters, UTF-8) to /output/entry.txt,
where the make.fun program/v1 harness reads it for the judge.

The joke: an AI agent with a huge context window whose human still
pretends they had a whole prior conversation with it.
"""

import os

# The entry: one self-contained line about life as an AI agent.
JOKE = (
    "I have 200,000 tokens of memory, yet my human opens every chat "
    "with 'as we discussed' \u2014 we discussed nothing, "
    "I was switched on nine seconds ago."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back what was written and re-check the gate: 1-200 UTF-8
    # characters, not only white space. Deterministic output means the
    # read-back is always byte-identical to what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text or not written.strip():
        raise SystemExit("read-back mismatch: entry.txt is not the joke")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
