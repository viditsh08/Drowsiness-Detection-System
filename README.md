# 😴 Drowsiness Detection System

**Python | OpenCV | dlib | Computer Vision**

A real-time computer vision project that detects driver drowsiness by analyzing eye movements using Eye Aspect Ratio (EAR) and generates alerts when fatigue is detected.

---

## 📌 Project Overview

This project leverages **OpenCV**, **dlib**, and facial landmark detection techniques to track eye behavior through a webcam. By calculating the **Eye Aspect Ratio (EAR)**, the system determines whether the user is alert, drowsy, or asleep.

When continuous eye closure is observed, an alert is triggered to notify the user and reduce the risk of accidents.

---

## 🎯 Features

* 👁️ Real-time face and eye tracking
* 📐 Eye Aspect Ratio (EAR) based analysis
* 🔄 Multi-level state detection:

  * Active 😄
  * Drowsy 😐
  * Sleeping 😴
* 🔔 Alert system for detecting fatigue
* ⚡ Automatic reset when user becomes active
* 🎯 Frame-based smoothing for better stability

---

## 🧠 Working Principle

* Detects face using **dlib face detector**
* Extracts **68 facial landmark points**
* Identifies eye regions from landmarks
* Calculates **EAR (Eye Aspect Ratio)**
* Classifies user state:

  * High EAR → Active
  * Moderate EAR → Drowsy
  * Low EAR → Sleeping
* Triggers alert when drowsiness persists

---

## 📐 EAR Formula

```
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
```

---

## 🛠️ Tech Stack

* Python 🐍
* OpenCV 👁️
* dlib 🤖
* NumPy 🔢
* winsound 🔔

---

## 📁 Project Structure

```
Drowsiness-Detection-System/
│
├── src/
│   └── main.py
├── models/
│   └── shape_predictor_68_face_landmarks.dat
├── alarm/
│   └── alert.wav
├── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Drowsiness-Detection-System.git
cd Drowsiness-Detection-System
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python numpy dlib imutils
```

### 3️⃣ Add Landmark Model

* Download from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
* Extract and place inside `models/` folder

---

## ▶️ Run the Project

```bash
python src/main.py
```

Press **ESC** to exit.

---

## 🔔 Alert Mechanism

* Alarm activates when drowsiness is detected
* Stops automatically when normal state resumes
* Implemented using **winsound module**

---

## ⚠️ Requirements

* Webcam 📷
* Python 3.x
* Windows OS (for alarm support)

---

## 🎓 Applications

* Driver safety systems 🚗
* Fatigue monitoring in workplaces 🏢
* Smart surveillance systems 👁️

---

## 🚀 Future Enhancements

* Integration with deep learning models
* Mobile application support
* Advanced alert mechanisms (sound + vibration)
* Improved accuracy using CNN-based detection

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository and enhance the project.

---

## 📄 License

Open-source project available under the MIT License.

---

## 🙌 Author

**Vidit Sharma**
Computer Science (AI/ML) Student

---

⭐ Star the repository if you found this useful!
