from ultralytics import YOLO
import os

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts"

def main():
    model = YOLO('yolov8n.pt')
    model.train(data=f'{dir_path}/dataset/dataset.yaml', epochs=1, imgsz=640, batch=1)

if __name__ == "__main__":
    main()