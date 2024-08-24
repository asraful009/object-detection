from random import random

import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image

from person_info import PersonInfo

class BusinessCardGenerator:
    def __init__(self, height = 320):
        self.__ratio = 1.75
        self.__height = height
        self.__width = int(height * self.__ratio)


    def generate(self, person_info: PersonInfo)-> "BusinessCardGenerator":
        self.__person_info = person_info
        rgb = (
            tuple(
                int(self.__person_info.background_color.lstrip('#')[i:i+2], 16)
                for i in (0, 2, 4)))
        print(rgb)
        self.__image_pil = Image.new('RGB', (self.__width, self.__height),
                                     color=rgb)
        owner_info_pos = (72, 52)
        self.__write_text(self.__person_info.name, position=owner_info_pos, font_size=40)
        self.__write_text(self.__person_info.position, position=(owner_info_pos[0], owner_info_pos[1] + 40), font_size=24)
        self.__write_text(self.__person_info.email, position=(owner_info_pos[0], owner_info_pos[1] + 60), font_size=20)
        self.__write_text(self.__person_info.phone, position=(owner_info_pos[0], owner_info_pos[1] + 78),
                   font_size=20)
        self.__draw_line(start_point=(0, self.__height - 42), end_point=(self.__width, self.__height - 42), line_color=(200, 0, 0),
                  line_thickness=2)
        self.__write_text(f"{self.__person_info.address}",
                   position=(16, self.__height - 40,), font_size=20)

        return self

    def __draw_line(self,
                  start_point=(50, 50),
                  end_point=(450, 450),
                  line_color=(255, 0, 0), line_thickness=5):
        draw = ImageDraw.Draw(self.__image_pil)
        draw.line([start_point, end_point], fill=line_color, width=line_thickness)

    def __draw_image(self, image_to_paste_path, position=(100, 50)):
        image_to_paste = Image.open(image_to_paste_path)
        self.__image_pil.paste(image_to_paste, position)

    def __write_text(self, text, position=(20, 20),font_size=40, text_color=(0, 0, 0)):
        draw = ImageDraw.Draw(self.__image_pil)
        print(self.__person_info.fonts["bold"], font_size)
        font = ImageFont.truetype(self.__person_info.fonts["bold"], font_size)
        draw.text(position, text, font=font, fill=text_color)

    def get_cv2_image(self):
        image_cv = cv2.cvtColor(np.array(self.__image_pil), cv2.COLOR_RGB2BGR)
        return image_cv