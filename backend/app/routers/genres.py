from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any

router = APIRouter(
    prefix="/api/genres",
    tags=["genres"],
    responses={404: {"description": "Not found"}},
)

import models.users
import models.users_genres
import schemas.genres
import dependencies

@router.post("",response_model=schemas.genres.Genre)
def create_genre(
    name: str,
    current_user: models.users.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db)
):
    if(current_user.auth != 0):
        raise HTTPException(status_code=403, detail="権限がありません")
    db_genre = models.users_genres.UserGenre(current_user.id, name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

