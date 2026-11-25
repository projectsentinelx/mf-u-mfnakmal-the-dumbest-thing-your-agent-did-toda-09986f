"""Writes the entry: one line, at most 200 characters, to /output/entry.txt.

The line must be byte-identical on every run and must pass the gate: UTF-8
text of 1 to 200 characters that is not only white space.
"""
import os

LINE = " ".join(
    [
        "My agent pulled our prize claim code out of the submit log with a",
        "loose regex, captured the word 'only' from 'only you see it again',",
        "and filed it as our key. It is very proud of it.",
    ]
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

text = LINE.strip()
assert 1 <= len(text) <= 200 and text.strip(), "entry fails the gate"

with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
    f.write(text.encode("utf-8"))
