import face_recognition
import cv2

# Load a sample picture and learn how to recognize it.
known_image = face_recognition.load_image_file(
    "DFA4869F-0F8B-4BFA-B6BA-724DC2A15635_1_201_a.jpeg")


known_face_encodings = face_recognition.face_encodings(known_image)

# Check if any faces were found in the image
if len(known_face_encodings) > 0:
    known_face_encoding = known_face_encodings[0]  # First face in the image
    # Proceed with your logic here
    print("Face encoding found!")
else:
    print("No faces found in the image.")
known_face_encoding = face_recognition.face_encodings(known_image)[0]
# Load another image to recognize
test_image = face_recognition.load_image_file(
    "nidhi.jpeg")

# Find all the faces and face encodings in the test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(
        [known_face_encoding], face_encoding)

    if matches[0]:
        print("It's a match!")
    else:
        print("No match found")
