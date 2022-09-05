from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

import models.users
import schemas.users
import services.users
import dependencies

@router.get("/me")
async def read_users_me(
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
):
    return current_user

@router.post("", response_model=schemas.users.User)
def create_user(
    user_create: schemas.users.CreateUser,
    db: Session = Depends(dependencies.get_db)
):
    user_create.hashed_password = services.users.get_password_hash(user_create.hashed_password)
    db_user = models.users.User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user