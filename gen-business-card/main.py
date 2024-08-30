
from person_info import PersonInfo
from business_card_generator import BusinessCardGenerator
import os
import json
import cv2
import random
import uuid

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
    file1 = open("train_1.txt", "a+")
    for image in images:
        p = PersonInfo(dir_path,
                       f"{image}",
                       f"{bg_images[random.randint(0, len(bg_images) - 1)]}",
                       "bn_BD")
        print(json.dumps(p.to_dict()))
        cv_image = bc_gen.generate(p).get_cv2_image()
        id = uuid.uuid4()
        cv2.imwrite(f"{dir_path}/business_cards/{index}.jpg", cv_image)
        index += 1
        # cv2.imshow("image", cv_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        file1.write(f"0 0.5 0.5 1.0 1.0\n")
        # exit(0)
        if index > 1000:
            break
    file1.close()

if __name__ == "__main__":
    main()