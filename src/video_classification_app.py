import os
import cv2
import streamlit as st
from ultralytics import YOLO


def extract_frames(video_path, frames_folder):
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, image = vidcap.read()
    count = 0

    while success:
        frame_path = os.path.join(frames_folder, f"frame{count:04d}.jpg")
        cv2.imwrite(frame_path, image)
        success, image = vidcap.read()
        count += 1

    return count, fps


def classify_frames_with_yolo(frames_folder, yolo_model_path, yolo_data_path, yolo_confidence, yolo_img_size):
    model = YOLO(yolo_model_path)
    frame_files = sorted(os.listdir(frames_folder))
    results_folder = os.path.join(frames_folder, 'results')
    os.makedirs(results_folder, exist_ok=True)

    for frame_file in frame_files:
        frame_path = os.path.join(frames_folder, frame_file)
        results = model(frame_path, task="detect", mode="predict", conf=yolo_confidence, imgsz=yolo_img_size)
        result_img_path = os.path.join(results_folder, frame_file)
        results[0].plot(save=True, filename=result_img_path)

    return results_folder


def create_video_from_frames(frames_folder, output_path, fps):
    frame_files = sorted(os.listdir(frames_folder))
    frame_files = [f for f in frame_files if f.endswith('.jpg')]

    if not frame_files:
        raise ValueError("No frames found in the provided folder.")

    first_frame_path = os.path.join(frames_folder, frame_files[0])
    frame = cv2.imread(first_frame_path)
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_file in frame_files:
        frame_path = os.path.join(frames_folder, frame_file)
        frame = cv2.imread(frame_path)
        video.write(frame)

    video.release()


st.title("Video Classification with YOLO")

uploaded_file = st.file_uploader("Upload a video to classify the frames using YOLO model.",
                                 type=["mp4", "avi", "mov", "mpeg"])

if uploaded_file is not None:
    if not os.path.exists("temp"):
        os.makedirs("temp")

    video_path = f"temp/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.video(video_path)

    frames_folder = "temp/frames"
    st.write("Extracting frames...")
    frame_count, fps = extract_frames(video_path, frames_folder)
    st.write(f"Extracted {frame_count} frames from the video at {fps} fps.")

    yolo_model_path = "runs/detect/train5/weights/best.pt"
    yolo_data_path = "data/data.yaml"
    yolo_confidence = 0.25
    yolo_img_size = 640

    st.write("Classifying frames with YOLO...")
    results_folder = classify_frames_with_yolo(frames_folder, yolo_model_path, yolo_data_path, yolo_confidence,
                                               yolo_img_size)
    st.write("Frame classification completed.")

    output_video_path = "temp/classified_video.avi"
    st.write("Creating classified video from frames...")
    create_video_from_frames(results_folder, output_video_path, fps)
    st.write("Classified video created successfully.")

    st.video(output_video_path)

    st.download_button(label="Download classified video", data=open(output_video_path, "rb").read(),
                       file_name="classified_video.avi")
