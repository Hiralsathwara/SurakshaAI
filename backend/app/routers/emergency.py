"""
===========================================================
                Emergency Help Router
===========================================================

Module:
    Emergency Help

Purpose:
    Provides immediate assistance workflow for scam victims.

Features:
    - Get emergency action checklist
    - Get bank helpline contacts
    - Submit fraud emergency report

===========================================================
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.emergency import (
    EmergencyReportCreate,
    EmergencyReportResponse,
    EmergencyChecklistResponse,
    BankContactResponse
)

from app.services import emergency_service


# ===========================================================
# Router Configuration
# ===========================================================

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency Help"]
)


# ===========================================================
# GET EMERGENCY CHECKLIST
# ===========================================================

@router.get(
    "/checklist",
    response_model=EmergencyChecklistResponse
)
def get_checklist():
    """
    Returns immediate actions a fraud victim should take.
    """

    return emergency_service.get_emergency_checklist()



# ===========================================================
# GET BANK CONTACTS
# ===========================================================

@router.get(
    "/banks",
    response_model=list[BankContactResponse]
)
def get_bank_contacts():
    """
    Returns bank customer care contact details.
    """

    return emergency_service.get_supported_banks()



# ===========================================================
# SUBMIT EMERGENCY REPORT
# ===========================================================

@router.post(
    "/report",
    response_model=EmergencyReportResponse,
    status_code=status.HTTP_201_CREATED
)
def submit_emergency_report(
        report: EmergencyReportCreate,
        db: Session = Depends(get_db)
):
    """
    Store fraud incident details submitted by user.
    """

    try:

        response = emergency_service.save_emergency_report(
            db=db,
            report=report
        )

        return response


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to submit emergency report: {str(e)}"
        )