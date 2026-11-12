# coolest-art-01 v4 — "One Stitch" (Round 2, recalibrated): deterministic copy of entry.png.
# v4 winner: a torn cream sky stitched back together with one crimson thread —
# black diagonal tear, red X stitches, thread curving into a horizon line,
# one tiny walker. First-glance distinct: light background in a dark feed.
# Writes the image to MAKEFUN_OUTPUT_DIR (default /output), byte-identical.
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
