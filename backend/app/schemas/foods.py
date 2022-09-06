from pydantic import BaseModel

class CreateFood(BaseModel):
    genre_id: int
    name: str
    img: str
    carbohydrate: int
    lipid: int
    protein: int
    mineral: int
    vitamin: int

class Food(CreateFood):
    id: int

    class Config:
        orm_mode = True