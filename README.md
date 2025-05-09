# 🔐 Face Recognition Login System

A simple and interactive **face recognition-based login and registration system** built using `Streamlit`, `streamlit-webrtc`, and `face_recognition`. This web app captures user face data through webcam, registers the user, and then allows login through real-time face authentication.

---

## 📸 Features

- 👤 **User Registration** with face capture
- ✅ **Login Authentication** via face recognition
- 🌐 Web-based UI using **Streamlit**
- 📷 Real-time webcam capture using **streamlit-webrtc**
- 🧠 Deep learning-based face encoding with **face_recognition**

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Webcam Integration**: [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc)
- **Face Recognition**: [face_recognition](https://github.com/ageitgey/face_recognition)
- **OpenCV**: For saving and handling image frames

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/face-auth-streamlit.git
   cd face-auth-streamlit
   ```

Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
OR install manually:

pip install streamlit streamlit-webrtc face_recognition opencv-python
▶️ Running the App

streamlit run app.py
Once the app starts, it will open in your browser at http://localhost:8501.

🧑‍💻 How It Works

1. Register
   Go to Register tab from the sidebar

Enter your name

Allow webcam access

Click Capture and Register – your face image will be saved to the known_faces/ directory

2. Login
   Go to Login tab

Click Capture and Login

If your face matches a registered user, you’ll be successfully logged in!
