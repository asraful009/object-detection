


import random
import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image, ImageChops

def main():
    im = Image.open('./../images/cards/white_image_0.jpg').convert('RGBA')
    im = im.rotate(random.randint(0, 359), expand=True)
    w, h = im.size
    im_bg = Image.new("RGBA", (w, h), (0, 0, 0, 0)).convert('RGBA')
    print(im.mode, im_bg.mode)
    if im.size != im_bg.size:
        print("ERROR")

    array1 = np.array(im)
    array2 = np.array(im_bg)
    xor_array = np.bitwise_xor(array1, array2)
    xor_image = Image.fromarray(xor_array, 'RGBA')

    xor_image.show()

if __name__ == "__main__":
    main()