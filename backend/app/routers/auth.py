from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from jose import jwt
from datetime import datetime, timedelta

import models.users
import schemas.users as users
import dependencies
from libs.auth import (
    verify_password,
    get_user,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


def _authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if user is None:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def _create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


router = APIRouter(
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/token", response_model=users.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(dependencies.get_db)
):
    user: models.users.PersonalUser | None = _authenticate_user(
        db, form_data.username, form_data.password
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = _create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
