from inference_sdk import InferenceHTTPClient
import cv2
import requests
import mysql.connector
from datetime import datetime
import os
import threading

# Roboflow API Client
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="nj2hBBqtpJKD11ULpQpN"
)

# ESP32 alarm endpoint
ESP32_IP = "http://172.20.10.3"  # ESP32 IP for alarm

# MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="swimsafe_ai"
)
cursor = db.cursor()

# Ensure static/detections exists
os.makedirs("static/detections", exist_ok=True)

# Video capture
cap = cv2.VideoCapture(0)

def list_cameras(max_cams=5):
    # Returns a list of available camera indices
    available = []
    for i in range(max_cams):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available

def stop_alarm_after_delay():
    try:
        requests.get(f"{ESP32_IP}/alarm/off")
    except Exception as e:
        print(f"ESP32 stop alarm failed: {e}")

def generate_frames(camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame to a temporary file for Roboflow API
        temp_img_path = "static/detections/temp.jpg"
        cv2.imwrite(temp_img_path, frame)
        try:
            result = CLIENT.infer(temp_img_path, model_id="swimmingxdrowning/4")
        except Exception as e:
            print("Roboflow API error:", e)
            continue

        found = False
        for p in result['predictions']:
            if p['class'] == 'Drowning' and p['confidence'] > 0.5:
                found = True
                x, y, w, h = int(p['x']), int(p['y']), int(p['width']), int(p['height'])
                cv2.rectangle(frame, (x-w//2, y-h//2), (x+w//2, y+h//2), (0,0,255), 2)
                cv2.putText(frame, f"Drowning {p['confidence']:.2f}",
                            (x - w//2, y - h//2 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        if found:
            # Save detection frame with unique filename in static/detections/
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            img_name = f"static/detections/{timestamp}.jpg"
            # Save the image
            saved = cv2.imwrite(img_name, frame)
            if saved:
                rel_img_path = img_name.replace("\\", "/")  # Ensure forward slashes
                # Use a new DB connection for each insert to avoid threading issues
                try:
                    db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="swimsafe_ai"
                    )
                    cursor = db.cursor()
                    cursor.execute(
                        "INSERT INTO history (timestamp, image_path) VALUES (NOW(), %s)",
                        (rel_img_path,)
                    )
                    db.commit()
                    cursor.close()
                    db.close()
                except Exception as db_exc:
                    print(f"DB insert failed: {db_exc}")
                # Trigger ESP32 alarm for 10 seconds
                try:
                    requests.get(f"{ESP32_IP}/alarm/on")
                    threading.Timer(10, stop_alarm_after_delay).start()
                except Exception as e:
                    print(f"ESP32 trigger failed: {e}")
            else:
                print(f"Failed to save detection image: {img_name}")

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()
