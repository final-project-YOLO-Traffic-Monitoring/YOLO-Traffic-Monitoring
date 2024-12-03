### **YOLOv8 Project Setup and Usage Guide**

### **Step 1: Install PyCharm**

1. **Open Your Web Browser:**
    - Open your preferred web browser (e.g., Chrome, Firefox, Safari).
2. **Go to the PyCharm Download Page:**
    - Navigate to the official PyCharm download page: [PyCharm Download](https://www.jetbrains.com/pycharm/download/).
3. **Select Your Operating System:**
    - On the download page, select your operating system from the options available (Windows, macOS, or Linux).
4. **Choose Community Edition:**
    - Community Edition: Free and open-source version ideal for learning and small projects.
    - Click on the Download button for the edition you want to install.
5. **Run the Installer:**
    - Follow the on-screen instructions to install PyCharm.
6. **Set Up Python Interpreter:**
    - Open PyCharm.
    - Go to File > Settings (or PyCharm > Preferences on macOS) and navigate to Project: &lt;project name&gt; > Python Interpreter.
    - Click the settings wheel, select Add, and then choose Virtual Environment. Specify Python 3.8 or later and create the environment.
7. **Create or Open a Project:**
    - You can now create a new project or open an existing one to start coding.

### **Step 2: Install Git**

1. **Visit the Official Git Website:**
    - Go to [Git Downloads](https://git-scm.com/downloads).
2. **Select Your Operating System:**
    - The website should automatically detect your OS, but if not, choose the appropriate version for your system (Windows, macOS, or Linux/Unix).
3. **Download the Installer:**
    - For Windows: Click the "Download" button for the latest version.
    - For macOS: Click on the latest version for your Mac (Intel or Apple Silicon).
    - For Linux: Follow the instructions for your specific distribution.
4. **Run the Installer:**
    - Windows: Open the downloaded .exe file and follow the installation wizard.
    - macOS: Open the .dmg file and follow the installation instructions.
    - Linux: Use the package manager commands provided on the Git website for your distribution.
5. **Verify the Installation:**

Open a terminal or command prompt and type:  
git --version

### **Step 3: Set Up the Python Environment**

1. **Install Required Packages:**
    - Open the terminal in PyCharm (usually at the bottom of the IDE).

Install YOLOv8 dependencies:  
pip install ultralytics

Install additional dependencies:  
pip install matplotlib tensorboard opencv-python pyyaml streamlit

By running pip install matplotlib tensorboard opencv-python pyyaml, you are equipping your Python environment with essential tools for data visualization, machine learning model tracking, image processing, and configuration management. These packages are foundational for a wide range of applications in data science, machine learning, computer vision, and software development.

### **Step 4: Clone YOLOv8 Repository**

1. **Clone the YOLOv8 Repo:**

In PyCharm's terminal, run:  
<br/>git clone <https://github.com/ultralytics/ultralytics.git>

cd ultralytics

pip install -e .

### **Step 5: Prepare Dataset**

1. **Place Your Dataset:**

- extract the vehicle dataset from the zip folder in the training_guide directory in the drive.
  - Ensure your dataset is accessible. Place the vehicle dataset folder inside the YOLOv8 directory or ensure the path in the training script points correctly to where the dataset resides.
  - Right-click on the "ultralytics" folder in PyCharm, then paste the "vehicle dataset" directory.

2. **Configure Dataset:**

In the ultralytics folder, open a new folder named “data” and inside it create a data.yaml file to reflect the correct paths and classes. Use the following content:  
<br/>train: ../vehicle dataset/train/images

val: ../vehicle dataset/valid/images

nc: 5

names: \['Car', 'Motorcycle', 'Truck', 'Bus', 'Bicycle'\]

### **Step 6: Train the Model**

**Run the Training Command:**

In the YOLOv8 directory within PyCharm’s terminal, run:

yolo task=detect mode=train data=data/data.yaml model=yolov8n.pt epochs=2 imgsz=640

### **Step 8: Evaluate and Use the Model**

1. **Run the Detection Script:**

Use the trained weights to detect objects in the test images. In the terminal, run:  
<br/>yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source="vehicle dataset/test/images/" conf=0.25 imgsz=640

2. **Review Results:**
    - The results of the detection will be saved in the runs/detect/predict\*/ directory. Review these output files to visually inspect the model's performance.
    - in runs/detect/train\*/ you will be able to see a more quantitative analysis, you can evaluate metrics like precision, recall, and mean Average Precision (mAP) using YOLOv8’s built-in evaluation tools.
    - Adjust parameters like the confidence threshold (--conf) and Intersection Over Union (IoU) threshold (--iou-thres) to fine-tune the balance between precision and recall.
