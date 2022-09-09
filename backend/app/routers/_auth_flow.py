from datetime import datetime, timedelta, timezone

import dependencies

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from libs.auth import generate_provisional_token, get_password_hash
from libs.mail import registration_mail_body, send_mail, password_reset_mail_body

from models.password_reset_queue import PasswordResetQueue
from models.users import User
import models.users
import schemas.users
import services.users
from models.users_provisional import ProvisionalUser

from pydantic import EmailStr

from schemas.auth import PasswordReset
from schemas.users import User

from sqlalchemy.orm import Session

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT


router = APIRouter(
    prefix="/api",
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

JST = timezone(timedelta(hours=+9), 'JST')

@router.post("/provisional_signup")
async def provisional_signup(
    req: Request,
    create_usr: schemas.users.CreateUser,
    db: Session = Depends(dependencies.get_db),
):
    # Check if given email address is already registered as `User`
    user = db.query(models.users.User).filter(create_usr.email == models.users.User.email).first()
    if user:
        raise HTTPException(
            HTTP_409_CONFLICT,
            "This address is already registered",
        )

    (token, expired_at) = generate_provisional_token()

    # Check if given email address is already registered as `ProvisionalUser`
    user = db.query(ProvisionalUser).filter(create_usr.email == ProvisionalUser.email).first()
    if user:
        user.token = token
        user.expired_at = expired_at
    else:
        password = services.users.get_password_hash(create_usr.hashed_password)
        user = ProvisionalUser(
            name=create_usr.name,
            email=create_usr.email,
            hashed_password=password,
            token=token,
            expired_at=expired_at,
        )
        db.add(user)

    db.commit()

    registration_url = f"""
    {req.base_url.scheme}://{req.base_url.hostname}:8080/mail?token={token}
    """

    body = registration_mail_body(
        mail_to=create_usr.email,
        registration_url=registration_url,
        valid_until=expired_at,
    )

    print(body)
    await send_mail(create_usr.email, "メールアドレスの仮登録を受け付けました", body)


# Which is better? path or query ?
@router.post("/auth_mail")
async def provisional_signup_email_verify(
    token: str, 
    db: Session = Depends(dependencies.get_db)
    ):
    user = db.query(ProvisionalUser).filter(ProvisionalUser.token==token).first()
    now = datetime.now(JST)
    time = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    if user and user.expired_at > time:
        # Prevent second attempt
        user.expired_at = datetime.now(JST)
        db_user = models.users.User(user.name, user.email,user.hashed_password)
        db.add(db_user)
        provisional_user = db.query(ProvisionalUser).filter(ProvisionalUser.token==token).first()
        db.delete(provisional_user)
        db.commit()
        return {"登録完了"}
    elif user and user.expired_at < time:
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "URL expired",
        )
    elif not user:
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "URL not found",
        )
    return


@router.post("/signup", response_model=User)
async def signup(
    name: str = Form(...),
    email: EmailStr = Form(...),
    password: str = Form(...),
    db: Session = Depends(dependencies.get_db),
):
    hashed_password = get_password_hash(password)
    db_user = User(email=email, name=name, hashed_password=hashed_password)
    db.add(db_user)

    provisional_user = db.query(ProvisionalUser).filter_by(email=email).first()
    db.delete(provisional_user)

    db.commit()
    return db_user


@router.post("/reset_password_challenge")
async def reset_password_request(
    req: Request,
    email: str = Form(...),
    db=Depends(dependencies.get_db),
):
    """
    Send a mail with password reset URL to given e-mail address.
    This is assumed to be used in case of forgetting login pasword.
    """
    # Check if given email address is already registered as `User`
    user = db.query(User).filter_by(email=email).first()
    if not user:
        print("user not found")
        # [TODO] Send this error to client side or not.
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "This address is not registered",
        )

    (token, expired_at) = generate_provisional_token()

    # Check if given email address is already registered as `ProvisionalUser`
    user = db.query(PasswordResetQueue).filter_by(email=email).first()
    if user:
        user.token = token
        user.expired_at = expired_at
    else:
        user = PasswordResetQueue(
            email=email,
            token=token,
            expired_at=expired_at,
        )
        db.add(user)

    db.commit()

    reset_url = f"""
    {req.base_url.scheme}://{req.base_url.hostname}/reset_password/{token}
    """

    body = password_reset_mail_body(mail_to=email, reset_url=reset_url, valid_until=expired_at)

    print(body)
    # await send_mail(email, "パスワードの再設定を受け付けました", body)

    return


@router.post("/reset_password/{token}")
async def reset_password_email_verify(token: str, db=Depends(dependencies.get_db)):
    """
    Verify clicked URL is valid or not.
    Response status 200 if given URL is valid, else status 400.
    """
    user = db.query(PasswordResetQueue).filter_by(token=token).first()
    if user and user.expired_at > datetime.now():
        # Prevent second attempt
        user.expired_at = datetime.now()
        db.commit()
        return user.email
    elif user and user.expired_at < datetime.now():
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "URL expired",
        )
    elif not user:
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "URL not found",
        )


@router.post("/reset_password")
async def reset_password(
    req: PasswordReset,
    db=Depends(dependencies.get_db)
):
    """
    Reset and update user's password.
    """
    user = db.query(User).filter_by(email=req.email).first()
    if not user:
        raise HTTPException(
            HTTP_400_BAD_REQUEST,
            "Invalid request(user not found)",
        )

    hashed_password = get_password_hash(req.password)
    user.hashed_password = hashed_password
    db.commit()
    return
