from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.oauth2 import get_current_user
from app.config.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.models.user import User



# from app.schemas.user_schema import (
#     UserCreate,
#     UserResponse,
#     Token,
# )
from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# -------------------- Register --------------------
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Create new user
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hash_password(user.password),
        language=user.language
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -------------------- Login --------------------
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # Find user by email
    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verify password
    if not verify_password(
        form_data.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    # Generate JWT Token
    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# -------------------- Profile --------------------
@router.get("/profile", response_model=UserResponse)
def profile(
    current_user: User = Depends(get_current_user)
):
    return current_user