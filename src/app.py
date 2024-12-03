import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
import yaml


# Load class names from data.yaml
def load_class_names(yaml_path):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['names']


# Path to your data.yaml file
yaml_path = 'data/data.yaml'


# Load class names
class_names = load_class_names(yaml_path)


# Load YOLOv8 model
model = YOLO('runs/detect/train5/weights/best.pt')


# Streamlit UI
st.title("YOLOv8 Object Detection")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    image_np = np.array(image)


    # Run YOLOv8 model
    results = model(image_np)


    # Display results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image_np, (x1, y1), (x2, y2), (0, 255, 0), 2)
            class_id = int(box.cls)
            class_name = class_names[class_id]
            label = f"{class_name} {float(box.conf):.2f}"
            cv2.putText(image_np, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    st.image(image_np, caption='Detected Image', use_column_width=True)

