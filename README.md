---

````markdown
<!-- ======================= HEADER SECTION ======================= -->

<h1 align="center">🤖 Smart Attendance System using DeepFace</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-RealTime%20Vision-green?logo=opencv" />
  <img src="https://img.shields.io/badge/DeepFace-ArcFace-red?logo=tensorflow" />
  <img src="https://img.shields.io/badge/License-MIT-orange" />
  <img src="https://img.shields.io/github/stars/ramtanay/Smart_Attendance_System?style=social" />
  <br/>
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20Ramtanay%20Chakraborty-ff69b4" />
</p>

<p align="center">
  <b>🎯 A Face Recognition based Smart Attendance System built with Python, OpenCV & DeepFace 🎯</b>  
  <br/> Automatically marks attendance through live webcam detection and saves it to daily CSV files.
</p>

---

## 🧠 Overview

The **Smart Attendance System** uses **DeepFace (ArcFace model)** for highly accurate face recognition.  
It detects faces in real time from a webcam and logs attendance automatically — no manual input required!  

📅 Each day, a new attendance file (e.g. `attendance_2025-11-02.csv`) is created automatically.

---

## 🚀 Features

✅ Real-time face detection with OpenCV  
✅ Recognition powered by DeepFace (ArcFace model)  
✅ Automatic daily attendance CSV files  
✅ Prevents duplicate entries per day  
✅ Super easy to add new people — just add their images!  
✅ Lightweight and fast  

---

## 🗂️ Folder Structure

```bash
Smart_Attendance_System/
│
├── dataset/
│   ├── Ramtanay_Chakraborty/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   └── Another_Person/
│       └── img1.jpg
│
├── attendance_YYYY-MM-DD.csv
├── app.py
├── requirements.txt
└── README.md
````

---

## ⚙️ Installation & Setup

### 🧩 Prerequisites

Make sure you have **Python 3.8+** installed.

### 🪄 Setup Steps

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ramtanay/Smart_Attendance_System.git
cd Smart_Attendance_System

# 2️⃣ Create a virtual environment
python -m venv venv

# 3️⃣ Activate it
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Run the app
python app.py
```

---

## 🧍‍♂️ Adding New People

1️⃣ Open the `dataset/` folder
2️⃣ Create a new folder with the **person’s name** (e.g., `Ramtanay_Chakraborty`)
3️⃣ Add 1–3 clear photos of the face
4️⃣ Run the program — the person will be recognized automatically next time!

---

## 🧾 Example Attendance Output

| Name                 | Date       | Time     |
| -------------------- | ---------- | -------- |
| Ramtanay Chakraborty | 2025-11-02 | 10:15:45 |
| Souvik Adhikari      | 2025-11-02 | 10:17:30 |

---

## 🎥 Live Detection Preview

| Box Color    | Meaning           |
| ------------ | ----------------- |
| 🟩 Green Box | Recognized Person |
| 🟥 Red Box   | Unknown Person    |

---

## 💡 Future Enhancements

🔹 GUI Dashboard to view attendance logs
🔹 Store attendance in MySQL / MongoDB
🔹 Email or Telegram notifications
🔹 Faster recognition using embedding cache
🔹 Cloud deployment with Flask/Streamlit

---

## 👨‍💻 Author

**Ramtanay Chakraborty**
🎓 B.Tech in Computer Science & Engineering
💡 AI, ML & Web Development Enthusiast
🏫 Durgapur Institute of Advanced Technology and Management
📧 [ramtanayc@gmail.com](mailto:ramtanayc@gmail.com)
🌐 [GitHub Profile](https://github.com/ramtanay)

---

## 🏷️ License

This project is licensed under the [MIT License](LICENSE).
You’re free to use, modify, and distribute this project with proper credit.

---

<p align="center">
  ⭐ If you found this project helpful, consider giving it a star on GitHub! ⭐  
  <br/>
  <img src="https://img.shields.io/github/stars/ramtanay/Smart_Attendance_System?style=social" />
</p>

<p align="center">
  Made with ❤️ by <b>Ramtanay Chakraborty</b>
</p>
```

---
