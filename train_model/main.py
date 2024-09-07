import os
import torch
from ultralytics import YOLO

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts"
device = 'cuda' if torch.cuda.is_available() else 'cpu'
def main():
    model = YOLO('yolov8n.pt')
    model.train(data=f'{dir_path}/dataset/dataset.yaml', epochs=1, imgsz=640, batch=10,
    device=device, pretrained=True)
    model.save(f'{dir_path}/dataset/custom_model.pt')
    # Load the image where you want to detect objects
    # image_path = f'{dir_path}/dataset/images/train/1.jpg'  # Replace with the path to your image
    # image = cv2.imread(image_path)

    # Perform object detection
    # results = model.predict(image)
    # print(results)
    # Visualize the results
    # for result in results:
    #     for box in result.boxes:
    #         x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
    #         label = result.names[box.cls]  # Get the label/class name
    #         confidence = box.conf[0]  # Get the confidence score
    #
    #         # Draw the bounding box on the image
    #         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #         text = f'{label} ({confidence:.2f})'
    #         cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Display the image with detected objects
    # cv2.imshow('YOLOv8 Object Detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()