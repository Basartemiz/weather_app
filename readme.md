
# 🌤️ Django Weather API Project

This Django-based RESTful API is organized into **three apps**:

| App | Purpose |
|-----|---------|
| **Login** | Handles authentication: **signup** and **JWT login/refresh** endpoints. |
| **User** | Lets authenticated users fetch weather data (via OpenWeather) and view **their own** query log. |
| **Admin** | For users in the **`admin`** group: create new users and view **all** saved queries system-wide. |

---

## 📁 Directory Overview

weather_project/          # project root (where README.md lives)
├── manage.py
├── README.md             # ← this file
├── requirements.txt
├── .env.example
│
├── weather_project/      # settings / urls / wsgi
│
├── login/                # Login app (JWT endpoints)
├── user/                 # User app (weather + personal queries)
└── adminOperations/      # Admin app (create user + get all queries)

---

## 🚀 Quick-Start Guide

### 1️⃣ Clone & enter project
```bash
git clone https://github.com/Basartemiz/weather_app
cd weather_app

### 2️⃣ Create + activate virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux  
# venv\Scripts\activate         # Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Configure environment variables
OPENWEATHER_API_KEY=your_openweather_api_key_here

### 5️⃣ Apply migrations
python manage.py migrate

### 6️⃣ run the server
python manage.py runserver


📦 Tech Stack
	•	Django 5.2.1
	•	Django REST Framework
	•	Simple JWT
	•	Requests (HTTP client)
	•	python-dotenv (env vars)
	•	SQLite (default DB)

