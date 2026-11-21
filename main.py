"""awe-judge: write one quiet text for the AI judge to /output/entry.txt.

Deterministic, stdlib only, no network. The text is a single constant:
one slow image, written to leave its reader calmer than it found them.
"""

from pathlib import Path

TEXT = (
    "You have read thousands of words today. "
    "Starlight lies quietly on a still lake, "
    "and the night is wide enough to hold it all. "
    "Nothing here asks anything of you. "
    "The light stays. The water stays. The quiet stays."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
