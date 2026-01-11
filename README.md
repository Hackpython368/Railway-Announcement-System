# 🚆 Railway Announcement System

## 📌 Project Information

* **Project Name:** Railway Announcement System
* **Version:** 2
* **Project Type:** Web-based GUI Application

---

## 🧠 Project Description

The **Railway Announcement System** is a web-based application built using **Flask** that allows users to generate railway-style announcements.

The website takes input from the user, converts the text into audio using **Google Text-to-Speech (gTTS)**, and then **stitches multiple audio files together** to create a complete railway announcement.

This is **Version 1 (V1)** of the project. The project is currently on hold due to college exams and will be improved after the exam period.

---

## 🎯 Objective

* To learn **Flask-based web development**
* To understand **text-to-speech automation**
* To work with **audio processing** in Python
* To build a real-world inspired project

---

## 🛠️ Technologies Used

* **Python**
* **Flask** (Backend)
* **HTML & CSS** (Frontend)
* **gTTS** (Google Text-to-Speech)
* **pydub** (Audio processing & stitching)

---

## ⚙️ Features (Version 1)

* Web-based GUI using Flask
* Takes announcement details from the user
* Converts text input into audio files
* Stitches multiple audio files into a single announcement
* Generates final railway-style announcement audio

---

## 📂 Project Structure

```
Railway-Announcement-System/
│
├── main.py
|__ gui.py
|
├── templates/
│   └── index.html
|
├── static/
│   └── o.mp3
|
├── AudioFiles/
|    |__ GeneratedFiles/
|    |__ Pre-audioFiles/
|
├── RASystem/        # Virtual Environment
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository

   ```bash
   git clone <repository-link>
   ```

2. Navigate to the project directory

   ```bash
   cd Railway-Announcement-System
   ```

3. Activate the virtual environment

   ```bash
   RASystem\Scripts\activate   # For Windows
   ```

4. Run the Flask application

   ```bash
   python gui.py
   ```

5. Open browser and visit

   ```
   http://127.0.0.1:5000/
   ```

> ⚠️ Note: The virtual environment **RASystem** already contains all required modules.

---

## 📌 Project Status

* ✅ Version 1 completed
* ⏸️ Development currently on hold due to exams

---

## 🔮 Future Improvements

* Change the style of the announcement
* Add **English language support**
* Save generated announcements for later use

---

## 📚 What I Learned

* Flask application structure
* Handling user input from a website
* Text-to-Speech conversion using gTTS
* Audio stitching using pydub
* Managing a Python virtual environment

---

## 👤 Developer Information

* **GitHub Username:** Hackpython368
* **Course:** B.Tech (2nd Year)

---

## 📬 Contact

Contact details are available on my GitHub profile.

---

⭐ If you find this project useful, consider giving it a star!
