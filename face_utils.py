# face_utils.py

import face_recognition
import numpy as np
import json
import os

USERS_DB = "users.json"

def load_users():
    if not os.path.exists(USERS_DB):
        with open(USERS_DB, 'w') as f:
            json.dump({}, f)
    with open(USERS_DB, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_DB, 'w') as f:
        json.dump(users, f)

def register_user(name, image_path):
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)
    if encoding:
        users = load_users()
        users[name] = encoding[0].tolist()
        save_users(users)
        return True
    else:
        return False

def authenticate_user(image_path):
    unknown_image = face_recognition.load_image_file(image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if not unknown_encodings:
        return None

    unknown_encoding = unknown_encodings[0]
    users = load_users()

    for name, encoding in users.items():
        known_encoding = np.array(encoding)
        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        if results[0]:
            return name
    return None
