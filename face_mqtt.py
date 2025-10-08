import cv2
import face_recognition
import os
import numpy as np
import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "10.178.13.231"  
MQTT_PORT = 1883
MQTT_TOPIC = "office/face_recognition"
mqtt_client = mqtt.Client()
try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Error: Could not connect to MQTT broker at {MQTT_BROKER}: {e}")
    exit()

authorized_persons = ["Ghannam", "George", "Salma", "Zyad"]

known_face_encodings = []
known_face_names = []

known_faces_dir = 'known_faces'

for person_name in authorized_persons:
    person_dir = os.path.join(known_faces_dir, person_name)
    if os.path.isdir(person_dir):
        for image_file in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(person_name)
    else:
        print(f"Warning: Directory {person_dir} not found. Create it and add images for {person_name}.")

print(f"Loaded {len(known_face_encodings)} face encodings for {len(authorized_persons)} persons.")

video_capture = cv2.VideoCapture(0)  

if not video_capture.isOpened():
    print("Error: Could not open webcam. Exiting.")
    exit()

face_match_tolerance = 0.6

last_message_time = 0
MESSAGE_COOLDOWN = 5  

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    access_granted = False
    recognized_name = "Unknown"
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=face_match_tolerance)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            recognized_name = known_face_names[best_match_index]
            access_granted = True
        
        box_color = (0, 255, 0) if recognized_name != "Unknown" else (0, 0, 255)
        
        cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)
        
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), box_color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, recognized_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
    current_time = time.time()
    if current_time - last_message_time > MESSAGE_COOLDOWN:
        if access_granted:
            message = f"GRANTED:{recognized_name}"
        else:
            message = "DENIED"
        mqtt_client.publish(MQTT_TOPIC, message)
        print(f"Published to {MQTT_TOPIC}: {message}")
        last_message_time = current_time

    status_text = "Access Granted!" if access_granted else "Access Denied"
    cv2.putText(frame, status_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if access_granted else (0, 0, 255), 2)
    
    cv2.imshow('Face Access System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
mqtt_client.disconnect()
