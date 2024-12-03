**Train YOLOv8 on Colab**

### step 1: Open Google Colab

1. Go to Google Colab.
2. Set Up the Environment:  
    Copy code:

!git clone <https://github.com/ultralytics/ultralytics.git>

%cd ultralytics

!pip install -e .

!pip install matplotlib tensorboard opencv-python pyyaml

1. Upload and Prepare Dataset:  
    from drive- [vehicle dataset](https://drive.google.com/drive/folders/1pZCMqynetfxrJ4FVlMBgN1FKWcNBCD9b?usp=drive_link). Mount Google Drive in Colab:  
    Copy code:  
    from google.colab import drive

drive.mount('/content/drive')

1. Create data Directory and Configure data.yaml:  
    Copy code:  
    import os

os.makedirs('data', exist_ok=True)

data_config = """

train: /content/drive/MyDrive/**your_dataset**/train/images

val: /content/drive/MyDrive/your_dataset/valid/images

nc: 5

names: \['Car', 'Motorcycle', 'Truck', 'Bus', 'Bicycle'\]

"""

with open('data/data.yaml', 'w') as f:

f.write(data_config)

step 2: Train the Model:  
Copy code  
!yolo task=detect mode=train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640

\*after its finish go to colab: files/ultratytics/runs/train/weights/best.pt  
and download this file and past it in your Pycharm dircatory project - ultratytics/runs
