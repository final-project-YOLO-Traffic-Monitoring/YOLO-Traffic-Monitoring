**Step-by-Step Guide to Create Application:**

first follow stages 1-5 in the YOLOv8 Project Setup and Usage Guide (inside the training_guide folder in the drive)

**Install the Required Packages:**

Ensure you have the necessary packages installed in your virtual environment:  
<br/>Copy code  
pip install ultralytics streamlit opencv-python

**Create the Streamlit Application:**

- copy the python files from the drive (app.py, video_classification_app.py) and paste them inside the ultralytics folder
- extract the train5 folder from the zip file in the drive and put it inside the pycharm project in this path: ultralytics/runs/detect/train5

In your terminal, navigate to the directory containing ultralytics and run

Copy code

- for images:

streamlit run app.py

- for videos:

streamlit run video_classification_app.py
