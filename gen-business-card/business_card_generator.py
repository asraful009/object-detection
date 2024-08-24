from random import random

import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image

from person_info import PersonInfo

class BusinessCardGenerator:
    def __init__(self):
        pass

    def generate(self, person_info: PersonInfo)-> "BusinessCardGenerator":
        self.__person_info = person_info
        rgb = (
            tuple(
                int(self.__person_info.background_color.lstrip('#')[i:i+2], 16)
                for i in (0, 2, 4)))
        print(rgb)
        self.__image_pil = Image.new('RGB', (320, 180),
                                     color=rgb)
        self.__write_text(self.__person_info.name)
        return self

    def __write_text(self, text, position=(20, 20),font_size=40, text_color=(0, 0, 0)):
        draw = ImageDraw.Draw(self.__image_pil)
        print(self.__person_info.fonts["bold"], font_size)
        font = ImageFont.truetype(self.__person_info.fonts["bold"], font_size)
        draw.text(position, text, font=font, fill=text_color)

    def get_cv2_image(self):
        image_cv = cv2.cvtColor(np.array(self.__image_pil), cv2.COLOR_RGB2BGR)
        return image_cv