# app.py

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import av
import os
import numpy as np
from face_utils import register_user, authenticate_user

st.set_page_config(page_title="Face Login System", layout="centered")
os.makedirs("known_faces", exist_ok=True)

class VideoCaptureTransformer(VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame = img.copy()
        return img

st.title("🔐 Face Recognition Login System")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
name = ""

if menu == "Register":
    st.subheader("Register")
    name = st.text_input("Enter your name")
    ctx = webrtc_streamer(key="register", video_transformer_factory=VideoCaptureTransformer)
    
    if st.button("Capture and Register"):
        if ctx.video_transformer and name:
            frame = ctx.video_transformer.frame
            if frame is not None:
                img_path = f"known_faces/{name}.jpg"
                cv2.imwrite(img_path, frame)
                if register_user(name, img_path):
                    st.success(f"User '{name}' registered successfully!")
                else:
                    st.error("Face not detected. Try again.")
            else:
                st.warning("No frame captured yet.")
        else:
            st.warning("Please enter a name and allow webcam access.")

elif menu == "Login":
    st.subheader("Login")
    ctx = webrtc_streamer(key="login", video_transformer_factory=VideoCaptureTransformer)
    
    if st.button("Capture and Login"):
        if ctx.video_transformer:
            frame = ctx.video_transformer.frame
            if frame is not None:
                img_path = "temp.jpg"
                cv2.imwrite(img_path, frame)
                user = authenticate_user(img_path)
                if user:
                    st.success(f"Welcome back, {user}!")
                else:
                    st.error("Face not recognized.")
            else:
                st.warning("No frame captured yet.")
