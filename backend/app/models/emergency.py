"""
===========================================================
              Emergency Help Database Model
===========================================================

Purpose:
    SQLAlchemy model for storing fraud emergency reports.

Stores:
    - User details
    - Bank details
    - Fraud transaction information
    - Incident description

===========================================================
"""


from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Text,
    DateTime
)

from datetime import datetime

from app.config.database import Base



# ===========================================================
# Emergency Report Model
# ===========================================================

class EmergencyReport(Base):

    """
    Database table for emergency fraud reports.
    """

    __tablename__ = "emergency_reports"


    # Primary Key

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # User Information

    name = Column(
        String(100),
        nullable=False
    )


    phone = Column(
        String(15),
        nullable=False
    )


    # Bank Information

    bank = Column(
        String(100),
        nullable=False
    )


    # Fraud Details

    amount = Column(
        Float,
        nullable=False
    )


    transaction_id = Column(
        String(100),
        nullable=False,
        unique=True
    )


    incident_date = Column(
        Date,
        nullable=False
    )


    description = Column(
        Text,
        nullable=False
    )


    # Record Creation Time

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )