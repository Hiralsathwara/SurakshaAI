from pydantic import BaseModel


class ScamRequest(BaseModel):
    message: str


class ScamResponse(BaseModel):
    message: str
    clean_text: str
    prediction: str
    confidence: float
    risk_level: str
    category: str
    explanation: str
    reasons: list[str]
    recommendations: list[str]