from pathlib import Path

workdir = Path("./projects/alg8-2")
number = len(list((workdir / Path("src")).glob("*"))) # Hopefully you didn't put anything unnecessary there
zfill_width = 3

# src_img_ext = "png"
src_img_ext = "jpg|gif"
sol_img_ext = "jpg"

