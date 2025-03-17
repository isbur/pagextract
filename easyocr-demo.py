import cv2
import easyocr
import numpy as np
from PIL import Image
from config import workdir

fileNumber = 1

reader = easyocr.Reader(['ru'], gpu=False)
# img = cv2.imread(f"{workdir}/src/{str(fileNumber).zfill(2)}.png")

# img = cv2.imread(f"{workdir}/src/{str(fileNumber).zfill(2)}.gif")

img_file = Image.open(f"{workdir}/src/{str(fileNumber).zfill(2)}.gif")
# width, height = img.size
# new_size = width*6, height*6
# img = img.resize(new_size, Image.LANCZOS)
# img = img.convert('L')
# img = img.point(lambda x: 0 if x < 230 else 255, '1')
# img = img.convert('RGB')
img = np.array(img_file)
result = reader.readtext(img, paragraph=True)
for r in result:
    box = r[0]
    A = [int(x) for x in box[0]]
    B = [int(x) for x in box[2]]
    cv2.rectangle(img, A, B, (0,0,255), 1)
    print(r)

cv2.namedWindow('img', cv2.WINDOW_FULLSCREEN)
cv2.imshow('img',img)
cv2.waitKey(0)