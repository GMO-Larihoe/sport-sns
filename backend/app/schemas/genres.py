from pydantic import BaseModel

class Genre(BaseModel):
    id: int
    user_id: int
    name: str

    class Config:
        orm_mode = True

class CreateGenre(BaseModel):
    genre_name: str
    food_name: str
    img: str
    carbohydrate: int
    lipid: int
    protein: int
    mineral: int
    vitamin: int
