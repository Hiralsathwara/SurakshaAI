import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.voice_service import (
    speech_to_text,
    analyze_voice,
    generate_response,
    text_to_speech,
    encode_audio_to_data_url,
)

router = APIRouter(
    prefix="/voice",
    tags=["Voice Assistant"],
)


@router.post("/analyze")
async def analyze_voice_message(
    file: UploadFile = File(...),
    language: str = Form("gu"),  # Accepts selected language code (default: Gujarati 'gu')
):
    suffix = os.path.splitext(file.filename)[1].lower() or ".wav"
    input_temp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    input_temp.close()

    wav_path = None
    audio_response_path = None

    try:
        # Save incoming file contents to temporary file
        with open(input_temp.name, "wb") as buffer:
            buffer.write(await file.read())

        # The frontend converts uploads to WAV and recordings are emitted as WAV,
        # so we expect a WAV-compatible audio file here.
        if suffix != ".wav":
            raise HTTPException(
                status_code=400,
                detail="Please upload WAV audio for voice analysis. The client should convert MP3/M4A to WAV before upload."
            )

        wav_path = input_temp.name

        # Process speech to text and analyze using language parameter
        text = speech_to_text(wav_path, language=language)
        result = analyze_voice(text, language=language)
        response_text = generate_response(result, language=language)
        
        audio_response_path = text_to_speech(response_text, language=language)
        audio_data_url = encode_audio_to_data_url(audio_response_path)

        return {
            "text": text,
            "language": language,
            "prediction": result.get("prediction", "Unknown"),
            "confidence": result.get("confidence", 0),
            "response": response_text,
            "audio": audio_data_url,
        }

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    finally:
        # Cleanup temporary files safely
        if os.path.exists(input_temp.name):
            os.remove(input_temp.name)
            
        if wav_path and wav_path != input_temp.name and os.path.exists(wav_path):
            os.remove(wav_path)
            
        if audio_response_path and os.path.exists(audio_response_path):
            os.remove(audio_response_path)