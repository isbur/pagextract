import os
from pathlib import Path
from config import workdir

for i in range(510, 1062+1):
    if not os.path.exists(workdir / Path("sol") / Path(str(i) + ".jpg")):
        print(i)