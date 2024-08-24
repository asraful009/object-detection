
from person_info import PersonInfo
from business_card_generator import BusinessCardGenerator
import os
import json
import cv2

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts"

def get_image_paths():
    images = []
    dir_image_path = dir_path + "/company_logo"
    for filename in os.listdir(dir_image_path):
        file_path = os.path.join(dir_image_path, filename)
        if os.path.isfile(file_path):
            images.append(file_path)
    return images

def main():
    images = get_image_paths()
    bc_gen = BusinessCardGenerator(320)
    for image in images:
        p = PersonInfo(dir_path, f"{image}", "bn_BD")
        print(json.dumps(p.to_dict()))
        cv_image = bc_gen.generate(p).get_cv2_image()
        cv2.imshow("image", cv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit(0)

if __name__ == "__main__":
    main()