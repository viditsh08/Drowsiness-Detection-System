import cv2
import numpy as np
import dlib
from imutils import face_utils
import winsound

# Initialize camera
cap = cv2.VideoCapture(0)

# Load models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Counters
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# Alarm control
alarm_on = False

# ----------- FINAL TUNED VALUES -----------
SLEEP_EAR = 0.20
DROWSY_EAR = 0.26

SLEEP_FRAMES = 15
DROWSY_FRAMES = 18
ACTIVE_FRAMES = 8
# -----------------------------------------

# EAR function
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# 🔔 Start alarm (continuous loop)
def start_alarm():
    winsound.PlaySound(
        "alarm.wav",
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    )

# 🛑 Stop alarm instantly
def stop_alarm():
    winsound.PlaySound(None, winsound.SND_PURGE)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    face_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()

        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Landmarks
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # Eyes
        leftEye = landmarks[36:42]
        rightEye = landmarks[42:48]

        # EAR calculation
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        # Draw eye contours
        cv2.polylines(face_frame, [leftEye], True, (0, 255, 0), 1)
        cv2.polylines(face_frame, [rightEye], True, (0, 255, 0), 1)

        # ----------- FINAL LOGIC -----------

        if ear < SLEEP_EAR:
            sleep += 1
            drowsy = 0
            active = 0

            if ear < 0.16 or sleep > SLEEP_FRAMES:
                status = "SLEEPING !!!"
                color = (255, 0, 0)

                # 🔔 Start alarm
                if not alarm_on:
                    alarm_on = True
                    start_alarm()

        elif SLEEP_EAR <= ear < DROWSY_EAR:
            drowsy += 1
            sleep = 0
            active = 0

            # 🛑 Stop alarm
            if alarm_on:
                alarm_on = False
                stop_alarm()

            if drowsy > DROWSY_FRAMES:
                status = "Drowsy !"
                color = (0, 0, 255)

        else:
            active += 1
            sleep = 0
            drowsy = 0

            # 🛑 Stop alarm
            if alarm_on:
                alarm_on = False
                stop_alarm()

            if active > ACTIVE_FRAMES:
                status = "Active :)"
                color = (0, 255, 0)

        # Display EAR
        cv2.putText(frame, f"EAR: {ear:.2f}", (300, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Display status
        cv2.putText(frame, status, (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        # Draw landmarks
        for (x, y) in landmarks:
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()