from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.oauth2 import get_current_user

from app.models.user import User
from app.models.scan_history import ScanHistory

from app.schemas.scam_schema import ScamRequest, ScamResponse
from app.services.scam_detection_service import scam_service

router = APIRouter(
    prefix="/detect",
    tags=["Scam Detection"]
)


@router.post(
    "",
    response_model=ScamResponse
)
def detect_scam(
    request: ScamRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Run AI prediction
    result = scam_service.predict(request.message)

    # Save scan history
    history = ScanHistory(
        user_id=current_user.id,
        message=result["message"],
        clean_text=result["clean_text"],
        prediction=result["prediction"],
        confidence=result["confidence"]
    )

    db.add(history)
    db.commit()

    return result