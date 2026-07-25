from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import Base, engine
from app.models.user import User

from app.routers import auth
from app.routers import scam_detector

from app.models.user import User
from app.models.scan_history import ScanHistory

from app.routers import history

from app.routers import dashboard

from app.routers import ocr

from app.routers import voice

from app.routers import chatbot

from fastapi import APIRouter, UploadFile, File, Form
from app.routers import emergency
from app.routers import financial_literacy


# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="SurakshaAI API"
)

# CORS Configuration
origins = [
    "http://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(scam_detector.router)
app.include_router(history.router)
app.include_router(dashboard.router)
app.include_router(ocr.router)
app.include_router(voice.router)
app.include_router(chatbot.router)
app.include_router(emergency.router)
app.include_router(financial_literacy.router)

# Root Route
@app.get("/")
def home():
    return {
        "message": "FastAPI Backend is Running 🚀"
    }

