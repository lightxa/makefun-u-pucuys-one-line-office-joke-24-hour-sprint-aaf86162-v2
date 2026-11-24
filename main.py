"""One-line office joke entry for make.fun.

Writes a single deadpan office joke to /output/entry.txt.
Gate (from the kit): UTF-8 text of 1 to 200 characters, not only
whitespace, a single line. This program self-checks that gate and
raises if the text fails it.
"""

import os
from pathlib import Path

ENTRY = (
    "The office microwave beeped for three hours yesterday "
    "because everyone assumed someone else would stop it."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Raise unless the text passes the kit's gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = ENTRY
    check_gate(text)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "entry.txt"
    out.write_text(text, encoding="utf-8")
    # Verify what was actually written, with no trailing newline.
    written = out.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written entry does not match the joke")
    check_gate(written)


if __name__ == "__main__":
    main()
