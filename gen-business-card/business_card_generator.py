

import random
import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image, ImageChops

from person_info import PersonInfo

class BusinessCardGenerator:
    def __init__(self, height = 320):
        self.__ratio = 1.75
        self.__height = height
        self.__width = int(height * self.__ratio)
        self.__person_info = None
        self.__image_pil = None


    def generate(self, person_info: PersonInfo)-> "BusinessCardGenerator":
        self.__person_info = person_info
        rgb = (
            tuple(
                int(self.__person_info.background_color.lstrip('#')[i:i+2], 16)
                for i in (0, 2, 4)))
        print(rgb)
        self.__image_pil = Image.new('RGBA', (self.__width, self.__height),
                                     color=rgb)
        owner_info_pos = (48, 52)
        self.__write_text(self.__person_info.name, position=owner_info_pos, font_size=40)
        self.__write_text(self.__person_info.position, position=(owner_info_pos[0], owner_info_pos[1] + 45), font_size=24)
        self.__write_text(self.__person_info.email, position=(owner_info_pos[0], owner_info_pos[1] + 76),
                          font_size=14, font_type="email")
        self.__write_text(self.__person_info.phone, position=(owner_info_pos[0], owner_info_pos[1] + 92),
                   font_size=16)
        self.__draw_line(start_point=(0, self.__height - 42), end_point=(self.__width, self.__height - 42),
                     line_color=(200, 0, 0),
                     line_thickness=2)
        self.__write_text(f"{self.__person_info.address}",
                   position=(16, self.__height - 40,), font_size=20)

        self.__draw_image(self.__person_info.logo_path, position=(380, 72))
        self.__write_text(text=f"{self.__person_info.company}", position=(220, 212), font_size=28)
        self.__write_text(text=f"{self.__person_info.company_email}", position=(220, 250), font_size=14, font_type="email")

        self.__draw_background()

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
    def __image_rotation(self, rotation = 0):
        im = self.__image_pil.rotate(rotation, expand=True, resample=Image.BICUBIC)
        w, h = im.size
        im_bg = Image.new("RGBA", (w, h), (0, 0, 0, 0)).convert('RGBA')
        array1 = np.array(im)
        array2 = np.array(im_bg)
        xor_array = np.bitwise_xor(array1, array2)
        xor_image = Image.fromarray(xor_array, 'RGBA')
        return xor_image

    def __draw_background(self):
        background_image = Image.open(self.__person_info.background_image)
        rotation_val = random.randint(0, 359)
        print(rotation_val)
        rotated_image_expanded = self.__image_rotation(rotation_val)
        w, h = rotated_image_expanded.size
        bw, bh = background_image.sizen
        bw, bh = random.randint(0, bw - w -640), random.randint(0, bh - h - 640)
        background_image = background_image.crop((bw, bh, bw + 640, bh +640))
        background_image.paste(rotated_image_expanded,
                               ((320 - int(w/2)), (320 - int(h/2))),
                                mask=rotated_image_expanded)

        self.__image_pil = background_image

    def __write_text(self, text, position=(20, 20),
                     font_size=40, text_color=(0, 0, 0),
                     font_type = "regular"):
        draw = ImageDraw.Draw(self.__image_pil)
        # print(font_type, self.__person_info.fonts[font_type])
        font = ImageFont.truetype(self.__person_info.fonts[font_type], font_size)
        draw.text(position, text, font=font, fill=text_color)

    def get_cv2_image(self):
        image_cv = cv2.cvtColor(np.array(self.__image_pil), cv2.COLOR_RGB2BGR)
        return image_cv