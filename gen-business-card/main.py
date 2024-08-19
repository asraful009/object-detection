
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from faker import Faker

class PersonInfo:
    def __init__(self, asserts_path, image="", locale="en_US"):
        self.__faker = Faker(locale)
        self.company = self.__faker.company()
        self.domain = self.__faker.domain_name()
        self.name = self.__faker.name()
        self.email = self.__faker.email(True, self.domain)
        self.phone = self.__faker.phone_number()
        self.position = self.__faker.job()
        self.company_email = self.__faker.email(True, self.domain)
        self.address = f"{self.__faker.building_number()} {self.__faker.street_name()} {self.__faker.country_code()}, {self.__faker.postcode()}"
        self.logo_path = image
        self.fonts = {}
        self.background_color = ["#FFF5E4", "#FFFBE6", "#F7F7F8", "#FFFBE6", "#ECFFE6",
                                 "#EEF7FF", "#E7FBE6"]
        if locale == "bn_BD":
            self.fonts["bold"] = f"{asserts_path}/fonts/bangla/Anek/AnekBangla-Bold.ttf"
            self.fonts["regular"] = f"{asserts_path}/fonts/bangla/Anek/AnekBangla-Regular.ttf"
            self.fonts["light"] = f"{asserts_path}/fonts/bangla/Anek/AnekBangla-light.ttf"
        else:
            self.fonts["bold"] = f"{asserts_path}/fonts/english/JetBrainsMono-Bold.ttf"
            self.fonts["regular"] = f"{asserts_path}/fonts/english/JetBrainsMono-Regular.ttf"
            self.fonts["light"] = f"{asserts_path}/fonts/english/JetBrainsMono-light.ttf"

    def to_dict(self):
        return {
            "company": self.company,
            "domain": self.domain,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "position": self.position,
            "company_email": self.company_email,
            "address": self.address,
            "logo_path": self.logo_path,
            "fonts": self.fonts
        }



class BusinessCardGenerator:
    def __init__(self):
        pass

    def generate(self, person_info: PersonInfo):
        self.__person_info = person_info
        rgb = tuple(int(self.__person_info.background_color[random.randint(0, len(self.__person_info.background_color) - 1)].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        self.__image_pil = Image.new('RGB', (320, 180),
                                     color=rgb)
        self.__write_text(self.__person_info.name)
        return self.__image_pil

    def __write_text(self, text, position=(20, 20),font_size=40, text_color=(0, 0, 0)):
        draw = ImageDraw.Draw(self.__image_pil)
        print(self.__person_info.fonts["bold"], font_size)
        font = ImageFont.truetype(self.__person_info.fonts["bold"], font_size)
        draw.text(position, text, font=font, fill=text_color)

    def get_cv2_image(self):
        image_cv = cv2.cvtColor(np.array(self.image_pil), cv2.COLOR_RGB2BGR)
        return image_cv


def write_text(image_pil,
               text = "",
               position=(20,20),
               font_path = "./asserts/fonts/JetBrainsMono-Regular.ttf",
               font_size = 40,
               text_color = (0, 0, 0) ):
    draw = ImageDraw.Draw(image_pil)
    print(font_path)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=text_color)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    font_bold_path = f"{dir_path}/../asserts/fonts/bangla/NotoSerifBengali-Bold.ttf"
    font_regular_path = f"{dir_path}/../asserts/fonts/bangla/NotoSerifBengali-Regular.ttf"
    font_light_path = f"{dir_path}/../asserts/fonts/bangla/NotoSerifBengali-Light.ttf"
    print(f"{dir_path}/asserts/fonts/bangla/")
    image_pil = Image.new('RGB', (320, 180), color='white')
    write_text(image_pil, text="পার্থক্য", position=(20, 20),
               font_path=font_light_path,
               font_size=40,
               text_color=(0, 0, 0))
    image_cv = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'{dir_path}/../images/cards/white_image_{0}.jpg', image_cv)

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts/"

def get_image_paths():
    images = []
    scale = .5
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        print(file_path)
        if os.path.isfile(file_path):
            images.append(file_path)

if __name__ == "__main__":
    images = get_image_paths()
    for 1 in range(10):
        p = PersonInfo()
