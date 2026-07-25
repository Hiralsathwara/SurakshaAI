"""
===========================================================
            Voice Assistant Service
===========================================================

Pipeline:

Audio
 ↓
Speech Recognition
 ↓
Text
 ↓
Scam Detection ML Model
 ↓
Response Generation
 ↓
Text To Speech

===========================================================
"""


import base64
import os
import tempfile

import speech_recognition as sr
from gtts import gTTS

from app.services.scam_detection_service import scam_service

import os
from pydub import AudioSegment

def convert_audio_to_wav(input_path: str, output_path: str):
    """Converts input audio file (MP3, M4A, WebM, etc.) to standard WAV format."""
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        return output_path
    except Exception as e:
        raise ValueError(f"Failed to convert audio file: {str(e)}")


# =====================================================
# Audio Encoding
# =====================================================
# The frontend converts uploaded audio to WAV before sending it to the backend.
# This avoids server-side FFmpeg/pydub dependencies and keeps the backend focused
# on speech recognition, scam analysis, and response generation.
# =====================================================

def encode_audio_to_data_url(audio_path: str) -> str:
    _, extension = os.path.splitext(audio_path)
    mime_type = "audio/mpeg" if extension.lower() in (".mp3", ".mpeg") else "audio/wav"
    with open(audio_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


# =====================================================
# Speech To Text
# =====================================================

def speech_to_text(audio_file, language_code="gu"):

    recognizer = sr.Recognizer()

    language_map = {
        "gu": "gu-IN",
        "hi": "hi-IN",
        "en": "en-IN",
        "mr": "mr-IN",
        "ta": "ta-IN",
        "te": "te-IN",
    }
    google_lang = language_map.get(language_code, "gu-IN")

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(
        audio,
        language=google_lang
    )

    return text




# =====================================================
# Scam Analysis
# =====================================================

def analyze_voice(text, language_code="gu"):

    result = scam_service.predict(text)
    result["language"] = language_code
    return result




# =====================================================
# Generate AI Response
# =====================================================

def generate_response(result, language_code="gu"):
    user_message = result.get("message", "")

    if language_code == "hi":
        if result["prediction"] == "Scam":
            return f"मैंने आपका संदेश सुना: '{user_message}'. यह संदेश धोखाधड़ी हो सकता है। कृपया OTP या बैंक विवरण साझा न करें।"
        return f"मैंने आपका संदेश सुना: '{user_message}'. यह संदेश सुरक्षित लगता है।"

    if language_code == "en":
        if result["prediction"] == "Scam":
            return f"I heard you say: '{user_message}'. This message may be a scam. Do not share OTP or bank details."
        return f"I heard you say: '{user_message}'. This message appears to be safe."

    if language_code == "mr":
        if result["prediction"] == "Scam":
            return f"मला तुमचा संदेश ऐकवला: '{user_message}'. हा संदेश फसवणूक असू शकतो. कृपया OTP किंवा बँक तपशील शेअर करू नका."
        return f"मला तुमचा संदेश ऐकवला: '{user_message}'. हा संदेश सुरक्षित दिसतो."

    if language_code == "ta":
        if result["prediction"] == "Scam":
            return f"நான் உங்கள் செய்தியை கேட்டேன்: '{user_message}'. இந்த செய்தி மோசடி இருக்கலாம். தயவுசெய்து OTP அல்லது வங்கி விவரங்களை பகிர வேண்டாம்."
        return f"நான் உங்கள் செய்தியை கேட்டேன்: '{user_message}'. இந்த செய்தி பாதுகாப்பாக தெரிகிறது."

    if language_code == "te":
        if result["prediction"] == "Scam":
            return f"నేను మీ సందేశాన్ని వినానని: '{user_message}'. ఈ సందేశం ఒక మోసం కావచ్చు. దయచేసి OTP లేదా బ్యాంక్ వివరాలను పంచుకోకండి."
        return f"నేను మీ సందేశాన్ని వినానని: '{user_message}'. ఈ సందేశం సురక్షితంగా కనిపిస్తుంది."

    if result["prediction"] == "Scam":
        return f"હું તમારો સંદેશ સાંભળ્યો: '{user_message}'. આ મેસેજ ફ્રોડ હોઈ શકે છે. કૃપા કરીને OTP, PIN અથવા બેંક માહિતી શેર કરશો નહીં."
    return f"હું તમારો સંદેશ સાંભળ્યો: '{user_message}'. આ મેસેજ સુરક્ષિત લાગે છે."




# =====================================================
# Text To Speech
# =====================================================

def text_to_speech(text, language_code="gu", target_path=None):
    file_path = target_path or tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name

    language_map = {
        "gu": "gu",
        "hi": "hi",
        "en": "en",
        "mr": "mr",
        "ta": "ta",
        "te": "te",
    }
    gtts_lang = language_map.get(language_code, "gu")

    audio = gTTS(
        text=text,
        lang=gtts_lang
    )

    audio.save(file_path)

    return file_path
