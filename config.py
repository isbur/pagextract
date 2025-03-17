from pathlib import Path

workdir = Path("./projects/alg9")
number = len(list((workdir / Path("src")).glob("*.png"))) # Hopefully you didn't put anything unnecessary there

sol_img_ext = "jpg"

