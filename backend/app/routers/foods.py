from fastapi import Response, status, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any

router = APIRouter(
    prefix="/foods",
    tags=["foods"],
    responses={404: {"description": "Not found"}},
)

import models.users
import models.users_genres
import models.foods
import schemas.foods
import services.img
import dependencies

@router.post("", response_model=schemas.foods.Food)
def create_food(
    create_food: schemas.foods.CreateFood,
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    if(current_user.auth != 0):
        raise HTTPException(status_code=403, detail="権限がありません")
    old_path = None
    img = services.img.save_icon_imag(create_food.img, old_path)
    db_food = models.foods.Food(create_food.genre_id, create_food.name, img, create_food.carbohydrate, create_food.lipid, create_food.protein, create_food.mineral, create_food.vitamin)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food
