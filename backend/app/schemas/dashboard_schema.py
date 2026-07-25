from pydantic import BaseModel


class DashboardSummary(BaseModel):

    total_scans: int

    scam_detected: int

    safe_messages: int

    success_rate: float