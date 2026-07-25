"""
===========================================================
                 Scan History Routes
===========================================================

Endpoints
---------
POST    /history/save
GET     /history
DELETE  /history/{history_id}

Features
--------
✓ User Authentication
✓ Search by Message
✓ Filter by Prediction
✓ Pagination
✓ Delete Scan History
===========================================================
"""

import math

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.oauth2 import get_current_user

from app.models.scan_history import ScanHistory
from app.models.user import User

from app.schemas.scan_history import ScanHistoryPagination


# ===========================================================
# Router Configuration
# ===========================================================

router = APIRouter(
    prefix="/history",
    tags=["Scan History"]
)


# ===========================================================
# Get User Scan History
# ===========================================================
# Supports:
# • Search
# • Prediction Filter
# • Pagination
# ===========================================================

@router.get(
    "",
    # response_model=list[ScanHistoryResponse]
    response_model=ScanHistoryPagination
)
def get_history(

    # Search text
    search: str | None = Query(
        default=None,
        description="Search message"
    ),

    # Prediction Filter
    prediction: str | None = Query(
        default=None,
        description="Scam / Safe / All"
    ),

    # Pagination
    page: int = Query(
        default=1,
        ge=1
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100
    ),

    # Dependencies
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):
    # ----------------------------------------
    # Calculate Pagination Offset
    # ----------------------------------------
    # total = query.count()
    # offset = (page - 1) * limit
    # total_pages = math.ceil(total / limit)

    # ----------------------------------------
    # Base Query
    # Only fetch current user's history
    # ----------------------------------------

    query = (
        db.query(ScanHistory)
        .filter(
            ScanHistory.user_id == current_user.id
        )
    )
  
    # ----------------------------------------
    # Search Filter
    # ----------------------------------------

    if search:
        query = query.filter(
            ScanHistory.message.ilike(f"%{search}%")
        )

    # ----------------------------------------
    # Prediction Filter
    # ----------------------------------------

    if prediction and prediction != "All":
        query = query.filter(
            ScanHistory.prediction == prediction
        )
    # ----------------------------------------
# Pagination Calculations
# ----------------------------------------

    total = query.count()

    offset = (page - 1) * limit

    total_pages = (
        math.ceil(total / limit)
        if total > 0
        else 1
    )

    # ----------------------------------------
    # Fetch History
    # ----------------------------------------

    history = (
        query
        .order_by(
            ScanHistory.created_at.desc()
        )
        .offset(offset)
        .limit(limit)
        .all()
    )

    # return history
    return {
    "items": history,
    "page": page,
    "limit": limit,
    "total": total,
    "total_pages": total_pages
}


# ===========================================================
# Delete Scan History
# ===========================================================

@router.delete("/{history_id}")
def delete_history(
    history_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # ----------------------------------------
    # Find History Record
    # ----------------------------------------

    history = (
        db.query(ScanHistory)
        .filter(
            ScanHistory.id == history_id
        )
        .first()
    )

    # ----------------------------------------
    # History Not Found
    # ----------------------------------------

    if not history:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )

    # ----------------------------------------
    # Authorization Check
    # ----------------------------------------

    if history.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to delete this history"
        )

    # ----------------------------------------
    # Delete History
    # ----------------------------------------

    db.delete(history)
    db.commit()

    return {
        "message": "History deleted successfully"
    }