"""
===========================================================
              Emergency Help Service
===========================================================

Purpose:
    Business logic for Emergency Help module.

Features:
    - Provide emergency checklist
    - Provide bank helpline details
    - Save fraud emergency reports

===========================================================
"""


from sqlalchemy.orm import Session

from app.models.emergency import EmergencyReport
from app.schemas.emergency import EmergencyReportCreate


# ===========================================================
# Emergency Action Checklist
# ===========================================================

def get_emergency_checklist():

    """
    Returns immediate steps a scam victim should follow.
    """

    return {
        "steps": [
            "Freeze your bank account immediately",
            "Block your UPI ID and payment services",
            "Call Cyber Crime Helpline 1930",
            "Report fraud at cybercrime.gov.in",
            "Contact your bank customer support",
            "Change banking passwords and UPI PIN",
            "Save screenshots and transaction details",
            "Do not delete scam messages or call records"
        ]
    }



# ===========================================================
# Bank Helpline Contacts
# ===========================================================

def get_supported_banks():

    """
    Returns common bank emergency contact numbers.

    Later this can be moved into database.
    """

    banks = [
        {
            "bank": "State Bank of India",
            "number": "1800112211"
        },
        {
            "bank": "HDFC Bank",
            "number": "18002586161"
        },
        {
            "bank": "ICICI Bank",
            "number": "18002662"
        },
        {
            "bank": "Axis Bank",
            "number": "18604195555"
        },
        {
            "bank": "Bank of Baroda",
            "number": "18002584455"
        }
    ]

    return banks



# ===========================================================
# Save Emergency Fraud Report
# ===========================================================

def save_emergency_report(
        db: Session,
        report: EmergencyReportCreate
):

    """
    Save user's fraud incident details into database.
    """

    emergency_report = EmergencyReport(

        name=report.name,

        phone=report.phone,

        bank=report.bank,

        amount=report.amount,

        transaction_id=report.transaction_id,

        incident_date=report.incident_date,

        description=report.description
    )


    db.add(emergency_report)

    db.commit()

    db.refresh(emergency_report)


    return {
        "id": emergency_report.id,
        "message": "Emergency report submitted successfully",
        "created_at": emergency_report.created_at
    }