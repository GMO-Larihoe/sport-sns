from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session, or_
from typing import List, Any

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

import models.users
import models.users_genres
import models.foods
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

@router.get("/genres")
def get_genres(
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    user_genre: dict[str, Any] = dict()
    db_admin = db.query(models.users.User).filter(models.users.User.auth == 0).first()
    db_genres = db.query(models.users_genres.UserGenre).filter(or_(models.users_genres.UserGenre.user_id == current_user.id, models.users_genres.UserGenre.user_id == db_admin.id)).all()
    for db_genre in db_genres:
        db_food = db.query(models.foods).filter(models.foods.Food.genre_id == db_genre.id).first()