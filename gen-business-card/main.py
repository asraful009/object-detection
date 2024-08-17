
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Card:
    def __init__(self):
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

if __name__ == "__main__":
    main()