# 🚆 Railway Announcement System – Version 2

A web-based **Railway Announcement System** built using **Flask**, designed to dynamically generate railway-style announcements and convert them into audio output.  
This project simulates real-world Indian railway announcements with improved **mobile responsiveness**, **input validation**, and **audio stability**.

---

## 🔥 Version 2 – What’s New

Version 2 focuses on real-world deployment issues and user experience improvements:

- ✅ Mobile-first responsive UI (desktop UI unchanged)
- 🔢 Input validation (numeric & text-only fields)
- 🔊 Stable audio playback (no overlapping on hosting)
- 🌐 Hosting-safe audio handling
- 📁 Clean and scalable project structure

---

## 🗂 Project Structure

```
Railway-Announcement-System/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── final_announcement.mp3
│
├── AudioFiles/
│   ├── GeneratedFiles/
│   └── Pre-GeneratedFiles/
│
├── Modules/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, Bootstrap 5, CSS  
- **Audio Handling:** HTML5 Audio API  
- **Deployment Ready:** Yes (Local & Hosted environments)

---

## 🎯 Features

- 🚆 Train announcement generation using user inputs
- 🔢 Train number accepts **numbers only**
- 🏙 Station names accept **letters only**
- 📱 Fully responsive UI for mobile devices
- 🔊 Audio playback without overlapping issues
- 🌐 Works correctly on hosted servers

---

## 🖥 How It Works

1. User enters:
   - Train Number
   - From Station
   - Via Station(s)
   - To Station
   - Platform Number
2. Flask processes the data
3. Announcement audio is generated
4. User listens to the announcement directly on the webpage

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Railway-Announcement-System.git
cd Railway-Announcement-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

### 4️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

---

## 📱 Mobile Optimization

- Touch-friendly buttons and inputs
- Responsive layout using media queries
- Numeric keypad for train number input
- Audio controls adapt to screen size

---

## 🔊 Audio Stability Fix

To resolve audio overlapping in hosted environments:

- Used a **single audio instance**
- Ensured playback only after user interaction
- Avoided multiple audio object creation

This approach mirrors real railway announcement systems.

---

## 🧪 Validation & Safety

- Frontend validation using HTML input patterns
- Backend validation recommended for production
- Relative file paths ensure hosting compatibility

---

## 📌 Future Enhancements

- 🌍 Multi-language announcements (Hindi / English)
- ⏱ Announcement queue system
- 🎧 Text-to-Speech integration
- 🌙 Dark / Light mode toggle
- 🚉 Real-time train data using APIs

---

## 🧠 Learning Outcomes

- Handling browser audio autoplay policies
- Debugging localhost vs hosted issues
- Building mobile-friendly production UIs
- Designing scalable Flask applications

---

## 👤 Author

**Vidya Pandey**  
Aspiring Software Engineer | Python & Web Development Enthusiast  

---

## 📄 License

This project is for educational and learning purposes only.
