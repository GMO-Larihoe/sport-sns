from database import SessionLocal
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from jose import JWTError, jwt
from libs.auth import (
    get_user,
    oauth2_scheme,
    SECRET_KEY,
    ALGORITHM
)
import schemas.users as users
import models.users


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def _get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload is None:
            raise credentials_exception
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = users.TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = get_user(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: models.users.User = Depends(_get_current_user)):
    if current_user.status != models.users.UserStatus.Active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
