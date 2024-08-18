
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from faker import Faker

class PersonInfo:
    def __init__(self, image = "", locale = "en_US"):
        self.__faker = Faker([locale])
        self.company = self.__faker.company()
        self.domain = self.__faker.domain_name()
        self.name = self.__faker.name()
        self.email = self.__faker.email(True, self.domain)
        self.phone = self.__faker.phone_number()
        self.position = self.__faker.job()
        self.company_email = self.__faker.company_email(True, self.domain)
        self.address = self.__faker.address()
        self.logo_path = image
    
    def __str__(self):
        return f""" "company": "{self.company}" \n 
            "domain": self.domain + "\n" + 
            self.name + "\n" + 
            self.email + "\n" + 
            self.phone + "\n" + 
            self.position + "\n" + 
            self.company_email + "\n" + 
            self.address + "\n" + 
            self.logo_path + "\n" + 
            """

class BusinessCardGenerator:
    def __init__(self):
        pass
    def generate(self, person_info: PersonInfo):
        pass

    def get_cv2_image(self):
        pass


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