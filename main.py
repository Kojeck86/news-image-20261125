#!/usr/bin/env python3
"""Copy the bundled front-page image to the output directory.

Standard library only. The program writes entry.png to /output/entry.png
by default (or $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set,
for local testing). The copy is byte-identical on every run: no network,
no clock, no randomness — the same bytes are written twice.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
