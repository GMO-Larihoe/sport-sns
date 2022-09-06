from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import datetime

from libs.auth import get_password_hash
import models.users
import error

def create_user(
    db: Session,
    name: str,
    email: str,
    password: str,
):
    try:
        hashed_password = get_password_hash(password)
        user = models.users.User(
            name=name,
            email=email,
            hashed_password=hashed_password,
        )
        db.add(user)
        db.flush()
    except SQLAlchemyError as sa:
        raise error.translate_orm_error(sa)