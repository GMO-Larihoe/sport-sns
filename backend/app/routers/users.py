from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from datetime import datetime, timedelta, timezone
from typing import List, Any

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

JST = timezone(timedelta(hours=+9), 'JST')

import models.users
import models.users_genres
import models.foods
import models.food_posts
import schemas.users
import schemas.genres
import schemas.food_posts
import schemas.foods
import services.users
import services.img
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

@router.post("/test", response_model=schemas.users.User)
def create_test_user(
    user_create: schemas.users.CreateUser,
    auth: int,
    db: Session = Depends(dependencies.get_db)
):
    user_create.hashed_password = services.users.get_password_hash(user_create.hashed_password)
    db_user = models.users.User(**user_create.dict())
    db_user.auth = auth
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/genres")
def get_genres(
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    user_genre: dict[str, List[dict[str, Any]]] = dict()
    db_admin = db.query(models.users.User).filter(models.users.User.auth == 0).first()
    db_genres = db.query(models.users_genres.UserGenre).filter(or_(models.users_genres.UserGenre.user_id == current_user.id, models.users_genres.UserGenre.user_id == db_admin.id)).all()

    for db_genre in db_genres:
        db_foods = db.query(models.foods.Food).filter(models.foods.Food.genre_id == db_genre.id).all()
        user_genre[db_genre.name] = list()
        for db_food in db_foods:
            food_dict = db_food.toDict()
            food_dict['img'] = services.img.change_imag_to_base64(food_dict['img'])
            user_genre[db_genre.name].append(food_dict)
        
    return user_genre

@router.post("/genres")
def create_genre(
    create_genre: schemas.genres.CreateGenre,
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    db_genre = db.query(models.users_genres.UserGenre).filter(and_(models.users_genres.UserGenre.user_id == current_user.id, models.users_genres.UserGenre.name == create_genre.genre_name)).first()
    old_path = None
    img = services.img.save_icon_imag(create_genre.img, old_path)
    if db_genre:
        has_food = db.query(models.foods.Food).filter(and_(models.foods.Food.genre_id == db_genre.id, models.foods.Food.name == create_genre.food_name)).first()
        if has_food:
            raise HTTPException(status_code=409, detail="既に登録済み")
        db_food = models.foods.Food(db_genre.id, create_genre.food_name, img, create_genre.carbohydrate, create_genre.lipid, create_genre.protein, create_genre.mineral, create_genre.vitamin)
    else:
        db_genre  = models.users_genres.UserGenre(current_user.id, create_genre.genre_name)
        db.add(db_genre)
        db.commit()
        db.refresh(db_genre)
        db_food = models.foods.Food(db_genre.id, create_genre.food_name, img, create_genre.carbohydrate, create_genre.lipid, create_genre.protein, create_genre.mineral, create_genre.vitamin)
    db.add(db_food)
    db.commit()
    return{"succsess"}

@router.post("/food_post")
def create_post(
    create_post: schemas.food_posts.CreatePost,
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    db_post = models.food_posts.FoodPost(current_user.id, create_post.genre_id, create_post.food_id, datetime.now(JST))
    db.add(db_post)
    db.commit()
    return {"成功！"}

@router.get("/food_post")
def get_post(
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    
    user_post: list[dict[str, Any]] = []
    now = datetime.now(JST)
    now_year = now.year
    now_month = now.month
    now_day = now.day
    day_start_time = datetime(now_year, now_month, now_day, 0, 0, 0)
    day_end_time = datetime(now_year, now_month, now_day, 23, 59, 59)
    db_posts = db.query(models.food_posts.FoodPost).filter(and_(models.food_posts.FoodPost.date >= day_start_time, models.food_posts.FoodPost.date <= day_end_time, models.food_posts.FoodPost.user_id == current_user.id)).all()
    for db_post in db_posts:
        user_dict: dict[str, Any] = dict()
        user_dict = db_post.toDict()
        db_genre = db.query(models.users_genres.UserGenre).filter(models.users_genres.UserGenre.id == db_post.genre_id).first()
        db_food = db.query(models.foods.Food).filter(models.foods.Food.id == db_post.food_id).first()
        food_dict = db_food.toDict()
        food_dict['img'] = services.img.change_imag_to_base64(food_dict['img'])
        user_dict.update(db_genre.toDict())
        user_dict.update(food_dict)
        user_dict.pop('user_id')
        user_post.append(user_dict)
    return user_post

@router.get("/nutritions", response_model=schemas.foods.Nutrition)
def get_nutritions(
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    nutritions: dict[str, int] = dict()
    now = datetime.now(JST)
    now_year = now.year
    now_month = now.month
    now_day = now.day
    day_start_time = datetime(now_year, now_month, now_day, 0, 0, 0)
    day_end_time = datetime(now_year, now_month, now_day, 23, 59, 59)
    db_posts = db.query(models.food_posts.FoodPost).filter(and_(models.food_posts.FoodPost.date >= day_start_time, models.food_posts.FoodPost.date <= day_end_time, models.food_posts.FoodPost.user_id == current_user.id)).all()
    carbohydrates = 0
    lipids = 0
    proteins = 0
    minerals = 0
    vitamins = 0
    for db_post in db_posts:
        db_food = db.query(models.foods.Food).filter(models.foods.Food.id == db_post.food_id).first()
        carbohydrates = db_food.carbohydrate + carbohydrates
        lipids = db_food.lipid + lipids
        proteins = db_food.protein + proteins
        minerals = db_food.mineral + minerals
        vitamins = db_food.vitamin + vitamins
    nutritions['carbohydrate'] = carbohydrates
    nutritions['lipid'] = lipids
    nutritions['protein'] = proteins
    nutritions['mineral'] = minerals
    nutritions['vitamin'] = vitamins
    return nutritions


    
