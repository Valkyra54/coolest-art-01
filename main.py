"""Coolest Art v5 — "Hourglass Waterfall": copy entry.png to the output directory.

Stdlib only. The output directory defaults to the absolute path /output
(overridable via MAKEFUN_OUTPUT_DIR); it is never a relative "out" folder,
so this program works even when the working directory is read-only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "entry.png"


def main() -> None:
    if not ENTRY.is_file():
        raise FileNotFoundError(f"entry.png not found at {ENTRY}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, output_dir / "entry.png")


if __name__ == "__main__":
    main()
