import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FasterRCNN_ResNet50_FPN_Weights
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

def draw_boxes(image, boxes, labels, scores, threshold=0.5):
    draw = ImageDraw.Draw(image)
    for box, label, score in zip(boxes, labels, scores):
        if score > threshold:
            draw.rectangle(box.tolist(), outline='red', width=3)
            print((box[0], box[1]), f'{label.item()} {score:.2f}')
            draw.text((box[0], box[1]), f'{label.item()} {score:.2f}', fill='green')
    return image

# Load a pre-trained Faster R-CNN model
model = fasterrcnn_resnet50_fpn(weights=FasterRCNN_ResNet50_FPN_Weights.COCO_V1)
model.eval()  # Set the model to evaluation mode

# Define a transformation to preprocess the input image
transform = T.Compose([
    T.ToTensor(),  # Convert the image to a tensor
])

directory_path = '/home/pavel/Pictures/archive/Images/Images' #os.getcwd() + '/images'
image_paths = []
scale = .5
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        image_paths.append(file_path)

for image_path in image_paths:
    image = Image.open(image_path)
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        predictions = model(image_tensor)
        boxes = predictions[0]['boxes']
        labels = predictions[0]['labels']
        scores = predictions[0]['scores']
        print(boxes, labels, scores)
        result_image = draw_boxes(image.copy(), boxes, labels, scores)

        # Display the result
        plt.imshow(result_image)
        plt.axis('off')
        plt.show()


