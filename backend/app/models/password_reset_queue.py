from datetime import datetime

from database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp


class PasswordResetQueue(Base):
    __tablename__ = "password_reset_queue"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), nullable=False, unique=True, index=True)
    token = Column(String(256), nullable=False, unique=True)
    created_at = Column(
        Timestamp,
        nullable=False,
        server_default=current_timestamp(),
    )

    expired_at = Column(Timestamp, nullable=False, server_default=current_timestamp())

    def __init__(self, email: str, token: str, expired_at: datetime) -> None:
        self.email = email
        self.token = token
        self.expired_at = expired_at
