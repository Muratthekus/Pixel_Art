import os
import numpy
import matplotlib
from PIL import Image

desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")


def runner(PATH):
    image = Image.open(PATH)
    image=image_crop(image)
    pixel_classification(image)


def image_crop(image):
    width, height = image.size
    while width % 25 != 0:
        width -= 1
    while height % 30 != 0:
        height -= 1
    image.crop((0, 0, width, height))
    return image


def pixel_classification(image):
    width,height = image.size
    pixel=image.load()
    RED=0
    GREEN=0
    BLUE=0
    for i in range(0,width,25):
        for j in range(0,height,30):

            for p in range(25):
                for k in range(30):
                    try:
                        RED += pixel[i + p, j + k][0]
                        GREEN += pixel[i + p, j + k][1]
                        BLUE += pixel[i + p, j + k][2]
                    except IndexError:
                        pass
            for p in range(25):
                for k in range(30):
                    try:
                        pixel[i + p, j + k] = (RED // 750, GREEN // 750, BLUE // 750)
                    except IndexError:
                        pass
            RED = 0
            GREEN = 0
            BLUE = 0


    rewrite_image(image)

def rewrite_image(image):
    image.save(desktop+"\simplify.png")


if __name__ == "__main__":
    runner(PATH=desktop + "\\" + input("Please write filename(ex: image.png)"))