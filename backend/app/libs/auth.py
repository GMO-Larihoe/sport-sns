from datetime import datetime, timedelta, timezone
from typing import Tuple
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models.users
import secrets


# [TODO] 環境変数から取得
SECRET_KEY = "GmEEMchaVRvSRYOkre937Me6puC6lQLSy3T0OkiQl2agaG9pgf6BnCOX7OPJY4oi"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JST = timezone(timedelta(hours=+9), 'JST')


def generate_provisional_token() -> Tuple[str, datetime]:
    token = secrets.token_urlsafe(36)
    return (token, datetime.now(JST) + timedelta(minutes=30))


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, email: str | None):
    if email is None:
        return None

    user = db.query(models.users.User).filter_by(email=email).first()
    return user
