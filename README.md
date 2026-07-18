# 🚗 Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection System built using **Python, OpenCV, dlib, and NumPy**. The system monitors the driver's eye movements using facial landmarks and calculates the **Eye Aspect Ratio (EAR)** to determine whether the driver is active, drowsy, or sleeping. If prolonged eye closure is detected, an alarm is triggered to alert the driver and help prevent accidents caused by fatigue.

---

## ✨ Features

- Real-time webcam-based monitoring
- Face detection using dlib
- 68 facial landmark detection
- Eye Aspect Ratio (EAR) calculation
- Detects three driver states:
  - 🟢 Active
  - 🟠 Drowsy
  - 🔴 Sleeping
- Continuous alarm for sleeping detection
- Real-time EAR display
- Facial landmark visualization

---

## 🛠️ Tech Stack

- Python
- OpenCV
- dlib
- NumPy
- imutils
- Winsound

---

## 📂 Project Structure

```
Driver-Drowsiness-Detection-System/
│
├── driver_drowsiness.py
├── shape_predictor_68_face_landmarks.dat
├── alarm.wav
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/viditsh08/Driver-Drowsiness-Detection-System.git
```

Navigate to the project directory

```bash
cd Driver-Drowsiness-Detection-System
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python driver_drowsiness.py
```

---

## 🧠 How It Works

1. Captures live video from the webcam.
2. Detects the driver's face using **dlib**.
3. Extracts 68 facial landmarks.
4. Calculates the **Eye Aspect Ratio (EAR)** for both eyes.
5. Classifies the driver's state into:
   - Active
   - Drowsy
   - Sleeping
6. Triggers an alarm when prolonged eye closure is detected.

---

## 📊 Driver State Classification

| State | Description |
|--------|-------------|
| 🟢 Active | Driver's eyes are open and the driver is alert. |
| 🟠 Drowsy | Driver's eyes remain partially closed for several consecutive frames. |
| 🔴 Sleeping | Driver's eyes remain closed beyond the defined threshold, triggering an alarm. |

---

## 🚀 Future Improvements

- MediaPipe Face Mesh integration
- Blink counter
- Head pose estimation
- Driver analytics dashboard
- Mobile notification support
- Deep learning-based fatigue detection

---

## 📚 Learning Outcomes

This project helped in understanding:

- Computer Vision fundamentals
- Face detection techniques
- Facial landmark detection
- Eye Aspect Ratio (EAR)
- Real-time video processing
- OpenCV image processing
- Python-based real-time applications

---

## 👨‍💻 Author

**Vidit Sharma**

GitHub: https://github.com/viditsh08

---

⭐ If you found this project useful, consider giving it a star.
