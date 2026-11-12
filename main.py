# coolest-art-01 v1 — "Koi to Dragon": deterministic copy of entry.png.
# Writes the image to MAKEFUN_OUTPUT_DIR (default /output), byte-identical.
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
