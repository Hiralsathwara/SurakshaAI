from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.oauth2 import get_current_user

from app.models.user import User

from app.schemas.dashboard_schema import DashboardSummary

from app.services.dashboard_service import dashboard_service


router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)


@router.get(

    "/summary",

    response_model=DashboardSummary

)
def dashboard_summary(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return dashboard_service.get_summary(

        db,

        current_user.id

    )

@router.get(
    "/trend"
)
def dashboard_trend(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return dashboard_service.get_weekly_trend(

        db,

        current_user.id

    )

@router.get(
    "/categories"
)
def dashboard_categories(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return dashboard_service.get_scam_categories(

        db,

        current_user.id

    )