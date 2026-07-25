"""
===========================================================
            Emergency Help Schemas
===========================================================

Purpose:
    Pydantic schemas for Emergency Help module.

Features:
    - Create emergency fraud reports
    - Validate user input
    - Return emergency report response

===========================================================
"""

from datetime import date, datetime
from pydantic import BaseModel, Field


# ===========================================================
# Create Emergency Report Request Schema
# ===========================================================

class EmergencyReportCreate(BaseModel):
    """
    Schema used when user submits a fraud emergency report.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="User full name"
    )

    phone: str = Field(
        ...,
        min_length=10,
        max_length=15,
        description="User contact number"
    )

    bank: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Bank name"
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Lost amount in INR"
    )

    transaction_id: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Fraud transaction ID"
    )

    incident_date: date = Field(
        ...,
        description="Date when fraud happened"
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Detailed fraud description"
    )


# ===========================================================
# Emergency Report Response Schema
# ===========================================================

class EmergencyReportResponse(BaseModel):
    """
    Schema returned after successful report submission.
    """

    id: int

    message: str

    created_at: datetime


    class Config:
        from_attributes = True


# ===========================================================
# Emergency Checklist Schema
# ===========================================================

class EmergencyChecklistResponse(BaseModel):
    """
    Immediate action checklist response.
    """

    steps: list[str]


# ===========================================================
# Bank Contact Schema
# ===========================================================

class BankContactResponse(BaseModel):
    """
    Bank helpline information.
    """

    bank: str

    number: str