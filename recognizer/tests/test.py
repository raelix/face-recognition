import re
import os
import sys
import face_recognition

folder_known = sys.argv[1]
unknown_image_in = sys.argv[2]

def scan_known_people(known_people_folder):
    known_names = []
    known_face_encodings = []

    for file in image_files_in_folder(known_people_folder):
        basename = os.path.splitext(os.path.basename(file))[0]
        img = face_recognition.load_image_file(file)
        encodings = face_recognition.face_encodings(img)
        known_names.append(basename)
        known_face_encodings.append(encodings[0])
    return known_names, known_face_encodings

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]



known_encoding_name, known_encoding_data = scan_known_people(folder_known)

unknown_image = face_recognition.load_image_file(unknown_image_in)

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Loop through each face in this frame of video
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    match = face_recognition.compare_faces(known_encoding_data, face_encoding)
    print match
    print known_encoding_name
