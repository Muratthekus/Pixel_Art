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
    while width % 120 != 0:  # 10 pixel for color, 2 pixel for divider
        width -= 1
    while height % 150 != 0:  # 10 pixel for color, 5 pixel for divider
        height -= 1
    image.crop((0, 0, width, height))
    return image


def pixel_classification(image):
    width,height = image.size
    pixel=image.load()
    RED=0
    GREEN=0
    BLUE=0
    for i in range(0,width,120):
        for j in range(0,height,150):

            for p in range(100):
                for k in range(100):
                    try:
                        RED += pixel[i + p, j + k][0]
                        GREEN += pixel[i + p, j + k][1]
                        BLUE += pixel[i + p, j + k][2]

                        for divide1 in range(2):
                            for divide2 in range(5):
                                try:
                                    pixel[i + p + divide1, j + k + divide2] = (255, 255, 255)
                                except IndexError:
                                    pass
                        # rewrite pixel value
                        pixel[i + p, j + k] = (RED // 10000, GREEN // 10000, BLUE // 10000)
                    except IndexError:
                        pass

    rewrite_image(image)

def rewrite_image(image):
    image.save(desktop+"\simplify.png")


if __name__ == "__main__":
    runner(PATH=desktop + "\\" + input("Please write filename(ex: image.png)"))
