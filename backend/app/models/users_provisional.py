from datetime import datetime, date

from database import Base

from sqlalchemy import Column, Integer, String, SmallInteger, Date, Boolean
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp


class ProvisionalUser(Base):
    __tablename__ = "provisional_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False, index=True)
    email = Column(String(64), nullable=False, unique=True, index=True)
    hashed_password = Column(String(128), nullable=False)
    token = Column(String(256), nullable=False, unique=True)
    created_at = Column(
        Timestamp,
        nullable=False,
        server_default=current_timestamp(),
    )

    expired_at = Column(Timestamp, nullable=False, server_default=current_timestamp())

    def __init__(self, name: str, email: str, hashed_password: str, token: str, expired_at: datetime) -> None:
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.token = token
        self.expired_at = expired_at
