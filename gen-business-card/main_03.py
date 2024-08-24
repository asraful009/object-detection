
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import os

def write_text(image_pil,
               text = "",
               position=(20,20),
               font_path = "/home/pavel/.fonts/Caveat-Regular.ttf",
               font_size = 40,
               text_color = (0, 0, 0) ):
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=text_color)


# Define the dimensions of the image (height, width)
ratio = 1.75
height = 320
width = int(height * ratio)
fake = Faker()

def draw_line(image_pil,
              start_point = (50, 50),
              end_point = (450, 450),
              line_color = (255, 0, 0), line_thickness = 5):
    draw = ImageDraw.Draw(image_pil)
    draw.line([start_point, end_point], fill=line_color, width=line_thickness)

def draw_image(image_pil, image_to_paste_path, position = (100, 50)):
    image_to_paste = Image.open(image_to_paste_path)
    image_pil.paste(image_to_paste, position)
def create_business_card(image_to_paste_path = '/home/pavel/Pictures/company_logo_archive_/logos/logos/AMTBB.png'):
    # Create a blank white image using Pillow
    image_pil = Image.new('RGB', (width, height), color='white')
    owner_info_pos = (72, 52)
    write_text(image_pil, text=fake.name(), position= owner_info_pos, font_size=40)
    write_text(image_pil, text=fake.job(), position=(owner_info_pos[0],owner_info_pos[1]+40), font_size=24)
    write_text(image_pil, text=fake.email(), position=(owner_info_pos[0],owner_info_pos[1]+60), font_size=20)
    write_text(image_pil, text=fake.phone_number(), position=(owner_info_pos[0],owner_info_pos[1]+78), font_size=20)
    draw_line(image_pil, start_point=(0, height-42), end_point=(width, height-42), line_color=(200,0,0), line_thickness=2)
    write_text(image_pil, text=f"{fake.street_address()}, {fake.city()}, {fake.country()}, {fake.postcode()}",
               position=(16, height-40,), font_size=20)

    draw_image(image_pil,
               image_to_paste_path,
                position = (380, 72))
    write_text(image_pil, text=f"{fake.company()}",
               position=(332, 212), font_size=28)
    write_text(image_pil, text=f"{fake.email()}",
               position=(332, 232), font_size=20)
    # Convert the Pillow image to OpenCV format
    image_cv = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    # Optionally, save the white image to a file
    return image_cv

directory_path = '/home/pavel/Pictures/company_logo_archive_/logos/logos/'
images = []
scale = .5
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    print(file_path)
    if os.path.isfile(file_path):
            images.append(file_path)
index = 0
for image in images:
    bc_im = create_business_card(image)
    cv2.imwrite(f'images/cards/white_image_{index}.jpg', bc_im)
    index += 1
    print(f'images/cards/white_image_{index}.jpg')

