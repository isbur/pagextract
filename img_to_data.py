import json
import os
import cv2 
from cv2.typing import MatLike
import easyocr
import numpy as np
from PIL import Image
from config import workdir, zfill_width
from msc import get_src_path


# def single_ocr(page_number: int) -> tuple[list, list]:
def single_ocr(page_number: int) -> list:
    
    real_path = get_src_path(page_number)
    
    img_file = Image.open(real_path)
    img = np.array(img_file)

    reader = easyocr.Reader(['ru'], gpu = False)

    paragraphs = reader.readtext(img, paragraph=True)
    # words = reader.readtext(img)

    # return (paragraphs, words)
    return paragraphs


def show(img: MatLike):
    #### Fullscreen by default
    cv2.namedWindow('img', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    ####
    cv2.imshow('img',img)
    cv2.waitKey(0)

    
def main() -> None:

    # for i in range(119, 233 + 1):
    #     pars, words = single_ocr(i)
    #     # Serializing json
    #     pars_json = json.dumps(pars, indent=4)
    #     words_json = json.dumps(words, indent=4)
    #     # Writing to *.json
    #     with open(f"{workdir}/pars/{str(i).zfill(zfill_width)}.json", "w") as outfile:
    #         outfile.write(pars_json)
    #     with open(f"{workdir}/words/{str(i).zfill(zfill_width)}.json", "w") as outfile:
    #         outfile.write(words_json)
    #     print("#", end="")
    # print()

    # for i in range(119, 233 + 1):
    for i in range(118, 118 + 1):
        pars = single_ocr(i)
        # Serializing json
        pars_json = json.dumps(pars, indent=4)
        # Writing to *.json
        with open(f"{workdir}/pars/{str(i).zfill(zfill_width)}.json", "w") as outfile:
            outfile.write(pars_json)
        print("#", end="")
    print()


if __name__ == "__main__":
    main()