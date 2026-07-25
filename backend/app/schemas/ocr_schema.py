from pydantic import BaseModel



class OCRResponse(BaseModel):

    extracted_text:str

    status:str

    confidence:int

    risk:str