I created a complete professional `README.md` for your **SurakshaAI** project including overview, features, architecture, modules, tech stack, setup instructions, API documentation reference, screenshots section, project structure, and future enhancements.

Save this file as:

```
README.md
```

```md id="58391"
# 🛡️ SurakshaAI  
## AI Powered Cyber Fraud Detection & Digital Safety Platform

![SurakshaAI Banner](https://img.shields.io/badge/AI-Cyber%20Security-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![React](https://img.shields.io/badge/Frontend-React-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Database](https://img.shields.io/badge/Database-MySQL-blue)


## 📌 Overview

**SurakshaAI** is an AI-powered Cyber Fraud Detection and Digital Safety Platform designed to protect users from modern online scams and cyber threats.

The platform combines:

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- OCR Technology
- Voice Assistance
- Cyber Safety Education

to help users detect suspicious messages, analyze fraud attempts, and take immediate action during cyber fraud situations.


## 🎯 Problem Statement

With the rapid growth of digital payments, online banking, and social media, cyber fraud incidents are increasing rapidly.

Common attacks include:

- OTP Fraud
- UPI Scams
- Phishing Messages
- Fake Investment Schemes
- Lottery Scams
- Fake Customer Support Fraud
- QR Code Fraud

Many users are unaware of these threats and do not know the correct steps after losing money.

SurakshaAI provides an intelligent solution for prevention, awareness, and emergency response.


# 🚀 Key Features


## 🤖 1. AI Scam Detection Engine

Detects fraudulent messages using Machine Learning.

### Capabilities:

✅ SMS Scam Detection  
✅ WhatsApp Message Analysis  
✅ Email Fraud Detection  
✅ Risk Level Prediction  
✅ Scam Category Identification  
✅ Confidence Score Generation  


Technology:

- TF-IDF Vectorization
- Machine Learning Classification
- NLP Text Processing


Example:

Input:

```

Your account will be blocked.
Share OTP immediately.

```

Output:

```

Prediction : Scam
Confidence : 97%
Risk Level : High
Category : OTP Fraud

```



---

# 📷 2. OCR Screenshot Scanner

Users can upload suspicious screenshots.

The system:

1. Extracts text from images
2. Processes extracted content
3. Sends data to AI Scam Detection Engine
4. Provides fraud prediction


Supported:

- PNG
- JPG
- JPEG


Technology:

- Tesseract OCR
- OpenCV
- Machine Learning


---

# 🆘 3. Emergency Help Module

Designed for users who have already lost money.

Provides instant guidance:

- Freeze Bank Account
- Call Bank Support
- Block UPI
- Cyber Crime Reporting
- Submit Fraud Report


Features:

✅ Emergency checklist  
✅ Bank helpline contacts  
✅ Fraud report submission  
✅ Transaction details storage  


---

# 📚 4. Financial Literacy Module

Cyber safety awareness section.

Provides educational content about:

- OTP Safety
- UPI Security
- Phishing Awareness
- Online Banking Safety
- Digital Payment Protection


Goal:

Educate users before they become victims.


---

# 🎙️ 5. Voice Assistant

Provides voice-based cyber safety assistance.

Features:

- Voice Input
- Speech Understanding
- Safety Guidance


Designed for:

- Elderly users
- Non-technical users
- Regional language support


---

# 💬 6. AI Cyber Security Chatbot

Interactive chatbot for cyber-related queries.

Users can ask:

- "Someone asked my OTP"
- "I clicked suspicious link"
- "How to block UPI?"


The assistant provides instant safety recommendations.


---

# 📊 7. Dashboard Analytics

Provides user security insights.

Dashboard includes:

- Total Scans
- Scam Detection Count
- Safe Messages
- Detection History
- Analytics Charts


---

# 🔐 8. User Authentication

Secure user management system.

Features:

- User Registration
- Login
- JWT Authentication
- Protected Routes
- Profile Management



---

# 🏗️ System Architecture


```

```
            User
             |
             |
      React Frontend
             |
             |
      FastAPI Backend
             |
-----------------------------
|            |              |
```

Machine      MySQL          AI Models
Learning    Database        NLP/OCR
|
Scam Detection Engine

```



# 🛠️ Technology Stack


## Frontend

- React.js
- Vite
- React Router
- CSS
- Chart.js


## Backend

- FastAPI
- Python
- SQLAlchemy
- JWT Authentication
- Pydantic


## Database

- MySQL


## Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- TF-IDF Vectorizer


## Computer Vision

- OpenCV
- Tesseract OCR


## Tools

- GitHub
- Postman
- MySQL Workbench
- VS Code / PyCharm



# 📂 Project Structure


```

SurakshaAI

│
├── backend
│
│   ├── app
│   │
│   ├── models
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── config
│   ├── database
│   └── main.py
│
│
├── frontend
│
│   ├── src
│   │
│   ├── api
│   ├── components
│   ├── pages
│   ├── services
│   └── App.jsx
│
│
├── ML Models
│
├── Dataset
│
└── README.md

````



# ⚙️ Installation & Setup


## Clone Repository


```bash
git clone https://github.com/yourusername/SurakshaAI.git

cd SurakshaAI
````

# Backend Setup

Navigate:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

# Frontend Setup

Navigate:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start application:

```bash
npm run dev
```

Frontend URL:

```
http://localhost:5173
```

# 🔑 Environment Variables

Create `.env` file.

Backend:

```
DATABASE_URL=mysql+pymysql://username:password@localhost/suraksha_ai

SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_api_key
```

Frontend:

```
VITE_API_URL=http://127.0.0.1:8000
```

# 📌 API Documentation

Complete API documentation is available here:

```
API_Documentation.md
```

Main API Categories:

* Authentication API
* Scam Detection API
* OCR API
* History API
* Emergency API
* Dashboard API
* Chatbot API
* Voice Assistant API

# 📈 Machine Learning Model

Dataset:

* Indian Cyber Scam Dataset
* Fraud Message Dataset
* SMS Spam Dataset

Training Pipeline:

```
Data Collection
        |
Data Cleaning
        |
Feature Engineering
        |
TF-IDF Vectorization
        |
Model Training
        |
Model Evaluation
        |
Prediction API

```

Model Performance:

```
Accuracy : 97.46%
```

# 🔒 Security Features

✅ JWT Authentication
✅ Protected Routes
✅ Secure API Access
✅ Fraud Detection AI
✅ User Data Protection
✅ Emergency Response Workflow

# 🌟 Future Enhancements

* Real-time cyber threat detection
* Gujarati/Hindi voice support
* Mobile Application
* Real-time bank fraud alerts
* Browser extension
* Advanced AI fraud prediction
* Government cybercrime API integration

# 👨‍💻 Developer

## Hiral Sathwara

B.Tech Information Technology Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Cyber Security
* Full Stack Development

# ❤️ Conclusion

SurakshaAI is not only a fraud detection system but a complete digital safety ecosystem that helps users:

✔ Detect scams
✔ Understand cyber threats
✔ Take emergency actions
✔ Learn safe digital practices

**Making digital transactions safer with Artificial Intelligence.**

```

This README is suitable for:
- ✅ GitHub repository
- ✅ Internship evaluation
- ✅ College project submission
- ✅ Final year project documentation
- ✅ Resume project showcase
- ✅ Viva presentation
```
