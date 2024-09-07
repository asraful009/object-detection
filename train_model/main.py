import os
import torch
from ultralytics import YOLO
import cv2

dir_path = f"{os.path.dirname(os.path.realpath(__file__))}/../asserts"
device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.cuda.empty_cache()
def main():
    if not os.path.exists(f'{dir_path}/dataset/custom_model_0.pt') or True:
        model_train = YOLO(f'{dir_path}/dataset/custom_model_0.pt')
        # print(model_train)
        # exit(0)
        itaration = 0
        while itaration >= 0:
            torch.cuda.empty_cache()
            model_train.train(data=f'{dir_path}/dataset/dataset.yaml', epochs=1, imgsz=640,
                              batch=1, half=True,
                              device=device, pretrained=True)
            model_train.save(f'{dir_path}/dataset/custom_model_{itaration}.pt')
            itaration = itaration - 1

    model = YOLO(f'{dir_path}/dataset/custom_model_0.pt')
    # Load the image where you want to detect objects
    image_path = f'{dir_path}/dataset/images/val/0_22.jpg'  # Replace with the path to your image
    image = cv2.imread(image_path)

    # Perform object detection
    results = model.predict(image)
    # print(results[0].boxes)
    # Visualize the results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            class_id = int(box.cls[0])
            label = ''
            if hasattr(result, 'names') and class_id in result.names:
                label = result.names[class_id]  # Get the label/class name
            else:
                label = f"Class {class_id}"  # Use default class ID if no label found

            confidence = box.conf[0].item()  # Convert tensor to float for confidence score

            # Draw the bounding box on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f'{label} ({confidence:.2f})'
            cv2.putText(image, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Display the image with detected objects
    cv2.imshow('YOLOv8 Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()