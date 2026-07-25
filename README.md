# 🛡️ SurakshaAI
## AI-Powered Scam Detection & Cyber Safety Platform

- please check DemoResult Folder to show the result

SurakshaAI is an **AI-powered cybersecurity platform** designed to protect users from online scams, fraud messages, phishing attempts, and digital threats.

The system combines **Machine Learning, Natural Language Processing (NLP), OCR, Voice Assistance, and Generative AI** to analyze suspicious content and provide users with instant safety recommendations.

The platform helps users identify fraudulent messages, scan suspicious screenshots, understand cyber risks, and interact with an AI assistant for cybersecurity guidance.

---

# 🚀 Project Overview

With the rapid growth of digital communication, cyber scams such as phishing, fake offers, OTP fraud, banking scams, and malicious links are increasing.

Many users cannot identify whether a message, screenshot, or online communication is genuine or fraudulent.

**SurakshaAI solves this problem by providing an intelligent cyber safety assistant that:**

- Detects scam messages using Machine Learning
- Analyzes suspicious text patterns
- Extracts text from screenshots using OCR
- Provides risk level and explanation
- Stores detection history
- Provides cybersecurity guidance through AI chatbot
- Supports voice-based interaction

---

# 🎯 Objectives

The main objectives of SurakshaAI are:

✅ Detect fraudulent and scam messages automatically  
✅ Provide real-time scam risk analysis  
✅ Educate users about cyber threats  
✅ Reduce online fraud through AI assistance  
✅ Create an intelligent cyber safety ecosystem  

---

# ✨ Key Features

## 🔐 1. User Authentication Module

Secure user management system.

Features:

- User Registration
- Login System
- JWT Authentication
- User Profile Management
- Secure Password Handling


---

# 🤖 2. AI Scam Detection Engine

The core module of SurakshaAI.

The system analyzes user messages and predicts whether the content is:

- Safe
- Suspicious
- Scam


### Machine Learning Pipeline

```
Raw Dataset
      |
      ↓
Data Cleaning
      |
      ↓
Text Preprocessing
      |
      ↓
Feature Extraction
(TF-IDF Vectorization)
      |
      ↓
Machine Learning Model
      |
      ↓
Prediction
      |
      ↓
Risk Analysis & Explanation
```

---

# 📊 Machine Learning Model

## Dataset Sources

The model was trained using multiple scam detection datasets:

- Indian Cyber Scam Hinglish Dataset
- Fraud Detection Dataset
- India Fraud Detection JSONL Dataset
- UCI SMS Spam Collection Dataset


## Dataset Statistics

```
Total Samples        : 6288

Training Samples     : 5028

Testing Samples      : 1258


Class Distribution:

Safe Messages        : 4626

Scam Messages        : 1662
```

---

# 🧠 Model Performance

Machine Learning Model:

```
Algorithm:
TF-IDF + Classification Model
```

Performance:

```
Accuracy: 97.46%
```

Saved Model Files:

```
scam_classifier.pkl

tfidf_vectorizer.pkl
```

---

# 📱 3. Scam Detection Dashboard

Users can:

- Enter suspicious messages
- Scan content
- View prediction result
- Check confidence score
- Understand scam category
- Receive safety recommendations


Example Output:

```
Prediction:
SCAM

Risk Level:
HIGH

Confidence:
96%

Reason:
Contains suspicious financial keywords
and phishing patterns.
```

---

# 📷 4. OCR Screenshot Scanner

The OCR module allows users to upload suspicious screenshots.

Workflow:

```
Screenshot Upload

        ↓

OCR Text Extraction

        ↓

Extracted Message

        ↓

AI Scam Detection

        ↓

Risk Report
```

Use cases:

- Fake payment screenshots
- Fraud messages
- Fake bank notifications
- Suspicious advertisements


Technology:

- Tesseract OCR
- Python OCR Processing

---

# 🎤 5. Voice Assistant Module

SurakshaAI provides voice-based interaction.

Features:

- Speech input
- Voice command processing
- Cyber safety assistance
- Gujarati language support (planned)


---

# 💬 6. AI Cybersecurity Chatbot

Integrated AI chatbot helps users with:

- Cybersecurity questions
- Scam awareness
- Safety guidance
- Fraud prevention tips


Capabilities:

- Natural language understanding
- Context-based responses
- Security recommendations


---

# 📈 7. Analytics Dashboard

Dashboard provides:

## Statistics

- Total scans
- Scam detections
- Safe messages
- User activity


## Visualizations

Implemented using:

- Chart.js
- React Charts


Dashboard Components:

```
Dashboard

 ├── Summary Cards

 ├── Detection Statistics

 ├── Weekly Trend Chart

 ├── Scam Distribution Chart

 └── User Activity
```

---

# 🏗️ System Architecture


```
                 User

                  |
                  |

          React Frontend

                  |

                  |

            FastAPI Backend

                  |

      -------------------------

      |                       |

 Authentication          AI Engine

      |                       |

 MySQL Database       ML Prediction Model

                              |

                      TF-IDF Vectorizer

                              |

                    Scam Classification

```

---

# 🛠️ Technology Stack


## Frontend

| Technology | Purpose |
|-|-|
| React.js | User Interface |
| Vite | Frontend Build Tool |
| JavaScript | Programming |
| CSS | Styling |
| Chart.js | Data Visualization |


---

## Backend

| Technology | Purpose |
|-|-|
| FastAPI | REST API Development |
| Python | Backend Logic |
| SQLAlchemy | ORM |
| MySQL | Database |
| JWT | Authentication |


---

## Artificial Intelligence

| Technology | Purpose |
|-|-|
| Scikit-learn | ML Model |
| TF-IDF | Text Feature Extraction |
| NLP | Text Processing |
| Pickle | Model Storage |


---

## Additional Technologies

- OCR
- Tesseract
- Google Gemini API
- OpenAI API
- GitHub


---

# 📂 Project Structure

```
SurakshaAI/

│
├── backend/
│
│   ├── app/
│   │
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── schemas/
│   ├── main.py
│   │
│   ├── scam_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   │
│   ├── requirements.txt
│   └── .env
│
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   ├── pages/
│   ├── services/
│   │
│   ├── package.json
│   └── vite.config.js
│
│
├── dataset/
│
├── screenshots/
│
├── API_Documentation.md
│
└── README.md

```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/SurakshaAI.git

cd SurakshaAI
```

---

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


Run FastAPI server:

```bash
uvicorn app.main:main --reload
```

Backend runs on:

```
http://localhost:8000
```

---

# Frontend Setup

Navigate:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run React application:

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🔑 Environment Variables

Create:

```
.env
```

Example:

```env
DATABASE_URL=mysql://username:password@localhost/surakshaai

JWT_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_api_key
```

---

# 🔌 API Endpoints


## Authentication

```
POST /register

POST /login

GET /profile
```


## Scam Detection

```
POST /detect
```

Request:

```json
{
 "message":"Congratulations! You won a lottery"
}
```


Response:

```json
{
 "prediction":"SCAM",
 "confidence":96,
 "risk":"HIGH"
}
```


## OCR Scanner

```
POST /ocr/scan
```


## Dashboard

```
GET /dashboard/statistics
```

---

# 🔒 Security Features

Implemented:

✅ JWT Authentication  
✅ Password Encryption  
✅ Secure API Communication  
✅ Scam Pattern Detection  
✅ Risk Analysis System  


---

# 🚀 Future Enhancements

Future improvements:

- Real-time fraud URL detection
- Browser extension
- Mobile application
- Multilingual scam detection
- Gujarati voice assistant improvement
- Live cyber threat database integration
- Advanced Deep Learning models


---

# 📸 Screenshots

(Add your screenshots)

```
screenshots/

├── login.png

├── dashboard.png

├── detector.png

├── ocr.png

└── chatbot.png
```

---

# 👨‍💻 Developer

**Hiral Sathwara**

B.Tech Information Technology Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Full Stack Development


---

# ⭐ Project Highlights

⭐ AI-Based Scam Detection  
⭐ 97.46% ML Accuracy  
⭐ FastAPI Backend  
⭐ React Dashboard  
⭐ OCR Integration  
⭐ AI Chatbot  
⭐ Cyber Safety Analytics  


---

# 📄 License

This project is developed for educational and research purposes.