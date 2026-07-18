# 🚗 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection System** built using **Python, OpenCV, dlib, NumPy, and imutils**. The system continuously monitors the driver's eye movements using facial landmark detection and calculates the **Eye Aspect Ratio (EAR)** to determine whether the driver is **Active**, **Drowsy**, or **Sleeping**. If prolonged eye closure is detected, an alarm is triggered to alert the driver and help reduce fatigue-related accidents.

---

## ✨ Features

- Real-time webcam monitoring
- Face detection using dlib
- 68-point facial landmark detection
- Eye Aspect Ratio (EAR) based fatigue detection
- Detects three driver states:
  - 🟢 Active
  - 🟠 Drowsy
  - 🔴 Sleeping
- Automatic alarm for sleeping detection
- Live EAR display
- Facial landmark visualization
- Lightweight and easy to run

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
├── alarm.wav
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/viditsh08/Drowsiness-Detection-System.git
```

### 2. Move into the project directory

```bash
cd Drowsiness-Detection-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Download Pre-trained Model

This project requires the **dlib 68 Facial Landmark Predictor**.

Download the model from the official dlib website:

**http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2**

### Steps

1. Download the `.bz2` file.
2. Extract it using **7-Zip** or **WinRAR**.
3. Copy the extracted file:

```
shape_predictor_68_face_landmarks.dat
```

4. Place it inside the project root directory.

Your final project structure should look like:

```
Driver-Drowsiness-Detection-System/
│
├── driver_drowsiness.py
├── shape_predictor_68_face_landmarks.dat
├── alarm.wav
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Run the Project

```bash
python driver_drowsiness.py
```

> **Note:** The application requires the `shape_predictor_68_face_landmarks.dat` file to be present in the project directory before execution.

---

## 🧠 How It Works

1. Captures live video from the webcam.
2. Detects the driver's face.
3. Extracts 68 facial landmarks.
4. Calculates the Eye Aspect Ratio (EAR) for both eyes.
5. Determines the driver's state:
   - Active
   - Drowsy
   - Sleeping
6. Plays an alarm when prolonged eye closure is detected.

---

## 📊 Driver State Classification

| State | Description |
|--------|-------------|
| 🟢 Active | Driver's eyes are open and the driver is alert. |
| 🟠 Drowsy | Eyes remain partially closed for several consecutive frames. |
| 🔴 Sleeping | Eyes remain closed beyond the threshold, triggering an alarm. |

---

## 🚀 Future Improvements

- MediaPipe Face Mesh integration
- Head pose estimation
- Blink rate analysis
- Deep learning-based fatigue detection
- Mobile notification support
- Performance optimization

---

## 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Computer Vision
- Face Detection
- Facial Landmark Detection
- Eye Aspect Ratio (EAR)
- Real-Time Video Processing
- OpenCV Applications
- Human Fatigue Detection

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vidit Sharma**

GitHub: https://github.com/viditsh08

---

⭐ If you found this project useful, consider giving it a star.
