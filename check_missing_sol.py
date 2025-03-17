import os
from pathlib import Path
from config import workdir

for i in range(583, 1040+1):
    if not os.path.exists(workdir / Path("sol") / Path(str(i) + ".jpg")):
        print(i)