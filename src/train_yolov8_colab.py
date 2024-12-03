# Train YOLOv8 on Colab

# Step 1: Open Google Colab and set up the environment
# Clone the YOLOv8 repository and install dependencies
!git clone https://github.com/ultralytics/ultralytics.git
%cd ultralytics
!pip install -e .
!pip install matplotlib tensorboard opencv-python pyyaml

# Step 2: Upload and Prepare Dataset
# Mount Google Drive to access the dataset
from google.colab import drive
drive.mount('/content/drive')

# Create a data directory and configure the data.yaml file for YOLOv8 training
import os

# Make a directory for data
os.makedirs('data', exist_ok=True)

# Configure the dataset paths and class names
data_config = """
train: /content/drive/MyDrive/your_dataset/train/images  # Path to training images
val: /content/drive/MyDrive/your_dataset/valid/images  # Path to validation images
nc: 5  # Number of classes
names: ['Car', 'Motorcycle', 'Truck', 'Bus', 'Bicycle']  # Class names
"""

# Save the configuration to data.yaml
with open('data/data.yaml', 'w') as f:
    f.write(data_config)

# Step 3: Train the Model
# Start training the YOLOv8 model
!yolo task=detect mode=train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640

# Note:
# After training completes, download the trained weights from:
# Colab directory: files/ultralytics/runs/train/weights/best.pt
# Save the file to your local PyCharm project directory:
# ultralytics/runs
