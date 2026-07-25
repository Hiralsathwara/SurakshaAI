from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ==================================================
# Create Scan History Schema
# ==================================================

class ScanHistoryCreate(BaseModel):
    message: str
    clean_text: str
    prediction: str
    confidence: float


# ==================================================
# Scan History Response Schema
# ==================================================

class ScanHistoryResponse(BaseModel):
    id: int
    user_id: int

    message: str
    clean_text: str

    prediction: str
    confidence: float

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==================================================
# Pagination Response Schema
# ==================================================

class ScanHistoryPagination(BaseModel):
    items: list[ScanHistoryResponse]

    page: int
    limit: int

    total: int
    total_pages: int