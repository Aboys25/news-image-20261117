"""Entry for make.fun news-image-20261117.

The entry is the bundled image (entry.png.b64: one line of base64 holding
JPEG bytes). This program decodes that line and writes the image where the
grader expects it, deterministically: it writes entry.png to
MAKEFUN_OUTPUT_DIR (or /output outside the grader).

Standard library only. No network, no randomness, no writes besides the
decoded image. The image is stored as a single base64 line so the entry
directory holds text files only.
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png.b64"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"bundled image missing: {SOURCE}")
    target_dir = OUTPUT_DIR.resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    if target.resolve() == SOURCE.resolve():
        return  # output would collide with the source; nothing to write
    data = base64.b64decode(SOURCE.read_bytes(), validate=True)
    if not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"):
        raise ValueError("bundled image is not a valid JPEG (SOI/EOI missing)")
    target.write_bytes(data)


if __name__ == "__main__":
    main()
