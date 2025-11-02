import cv2
from deepface import DeepFace
import numpy as np
import os
import pandas as pd
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Configuration
DATASET_DIR = "dataset"
MODEL = "ArcFace"
THRESHOLD = 0.35   # cosine similarity threshold (higher = looser)
EMBEDDING_SIZE = 512

# Create attendance folder
if not os.path.exists("attendance"):
    os.makedirs("attendance")

# Create today's attendance file
today = datetime.now().strftime("%Y-%m-%d")
attendance_path = os.path.join("attendance", f"attendance_{today}.csv")
if not os.path.exists(attendance_path):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(attendance_path, index=False)
else:
    df = pd.read_csv(attendance_path)

def mark_attendance(name):
    global df
    date_today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    if not ((df["Name"] == name) & (df["Date"] == date_today)).any():
        df = pd.concat([df, pd.DataFrame([[name, date_today, time_now]], columns=["Name", "Date", "Time"])], ignore_index=True)
        df.to_csv(attendance_path, index=False)
        print(f"[ATTENDANCE] {name} marked present at {time_now}")

# ------------------------------
# Step 1: Load known face embeddings once
# ------------------------------
print("[INFO] Loading known face embeddings...")
known_embeddings = []
known_names = []

for person in os.listdir(DATASET_DIR):
    person_path = os.path.join(DATASET_DIR, person)
    if not os.path.isdir(person_path):
        continue

    for img_name in os.listdir(person_path):
        if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(person_path, img_name)
            try:
                emb = DeepFace.represent(img_path=img_path, model_name=MODEL, enforce_detection=False)[0]["embedding"]
                known_embeddings.append(emb)
                known_names.append(person)
            except Exception as e:
                print(f"[ERROR] Failed embedding for {img_name}: {e}")

known_embeddings = np.array(known_embeddings)
print(f"[INFO] Loaded embeddings for {len(known_names)} images of {len(set(known_names))} people.")

# ------------------------------
# Step 2: Start Webcam
# ------------------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("[ERROR] Webcam not accessible.")
    exit()
print("[INFO] Webcam started successfully.")

# ------------------------------
# Step 3: Real-time detection
# ------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6, minSize=(100, 100))

    for (x, y, w, h) in faces:
        face_roi = frame[y:y + h, x:x + w]
        try:
            # Get embedding for the detected face
            emb = DeepFace.represent(face_roi, model_name=MODEL, enforce_detection=False)[0]["embedding"]

            # Compute cosine similarities
            sims = cosine_similarity([emb], known_embeddings)[0]
            best_match_idx = np.argmax(sims)
            best_match_score = sims[best_match_idx]
            recognized_name = known_names[best_match_idx] if best_match_score > THRESHOLD else "Unknown"

            # Mark attendance
            if recognized_name != "Unknown":
                mark_attendance(recognized_name)

            # Draw
            color = (0, 255, 0) if recognized_name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{recognized_name} ({best_match_score:.2f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        except Exception as e:
            print(f"[ERROR] Detection error: {e}")

    cv2.imshow("Smart Attendance System (Optimized)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Exited cleanly.")
