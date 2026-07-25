from fastapi import APIRouter, UploadFile, File

import os
import uuid


from app.services.ocr_service import (
    extract_text,
    detect_scam
)


router = APIRouter(
    prefix="/ocr",
    tags=["OCR Scanner"]
)



UPLOAD_FOLDER="uploads/screenshots"


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)



@router.post("/scan")
async def scan_screenshot(
    file:UploadFile = File(...)
):


    file_name = (
        str(uuid.uuid4())
        +"_"
        +file.filename
    )


    file_path=os.path.join(
        UPLOAD_FOLDER,
        file_name
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )



    text = extract_text(
        file_path
    )



    result = detect_scam(
        text
    )


    return {


        "extracted_text":text,


        "scam_result":result


    }