
import sys
from ultralytics import YOLO
import cv2
import torch
import matplotlib.pyplot as plt
import numpy as np
import os

def edge_detected(image):
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        im_canny = cv2.Canny(im_gray, 50, 150)
        im_blurred = cv2.GaussianBlur(im_gray, (5, 5), 0)
        im_edges = cv2.Canny(im_blurred, 50, 150)
        return im_gray, im_canny, im_blurred, im_edges

def get_model():
    model = torch.load('yolov10x.pt')
    return model

def main():
    directory_path = os.getcwd() + '/images'
    images = []
    scale = .5
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        print(file_path)
        if os.path.isfile(file_path):
                images.append(file_path)
    rows = []
    for image in images:
        file_name = os.path.basename(file_path)
        print(f"{ image }")
        results = get_model()(image)
        print(len(results))
        # for result in results:
        #     result.show()
        # break
        # image = cv2.imread(image)
        # image = cv2.resize(image, (320, 240), interpolation=cv2.INTER_LINEAR)

        # g, c, b, e = edge_detected(image)
        # im_edges = cv2.cvtColor(e, cv2.COLOR_GRAY2BGR)
        # # np.hstack((image, im_edges))
        # rows.append(np.hstack((image, im_edges)))
    # grid_image = np.vstack(rows)
    #
    # cv2.imshow('Image', grid_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()