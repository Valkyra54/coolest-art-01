# coolest-art-01 v3 — "The Volcano Tree" (signature-first): deterministic copy of entry.png.
# v3 winner: the eruption IS a tree — lava limbs, ember leaves, fire crown,
# one colossal silhouette on a dark starry sky, tiny sleeping village at the base.
# Writes the image to MAKEFUN_OUTPUT_DIR (default /output), byte-identical.
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
