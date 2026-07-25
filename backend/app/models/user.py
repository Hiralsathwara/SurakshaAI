from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from app.config.database import Base

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(15))

    password = Column(String(255), nullable=False)

    language = Column(String(30))

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    scan_history = relationship(
    "ScanHistory",
    back_populates="user",
    cascade="all, delete-orphan"
)