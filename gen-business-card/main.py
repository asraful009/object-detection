
from person_info import PersonInfo
from business_card_generator import BusinessCardGenerator
import os
import cv2
import random
import numpy as np

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts"

def get_image_paths(dir_image_path):
    images = []
    for filename in os.listdir(dir_image_path):
        file_path = os.path.join(dir_image_path, filename)
        if os.path.isfile(file_path):
            images.append(file_path)
    return images

def main():
    images = get_image_paths(dir_path + "/company_logo")
    bg_images  = get_image_paths(dir_path + "/background_images")
    bc_gen = BusinessCardGenerator(320)
    index = 0
    for image in images:
        rotations = np.random.randint(0, 359, size=10)
        for rotation in rotations:
            ix_str = f"{index}_{rotation}"
            p = PersonInfo(dir_path,
                           f"{image}",
                           f"{bg_images[random.randint(0, len(bg_images) - 1)]}",
                           "bn_BD")
            # print(json.dumps(p.to_dict()))
            bc_gen.generate(p, rotation)
            cv_image = bc_gen.get_cv2_image()
            card_location = bc_gen.get_card_location()
            w, h = card_location[1][0]/640, card_location[1][1]/640
            cv2.imwrite(f"{dir_path}/dataset/images/train/{ix_str}.jpg", cv_image)
            with open(f'{dir_path}/dataset/labels/train/{ix_str}.txt', 'w') as file:
                file.write(f"0 0.5 0.5 {w} {h}")
            index += 1
            # cv2.imshow("image", cv_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # exit(0)
        if index > 0:
            break


if __name__ == "__main__":
    main()