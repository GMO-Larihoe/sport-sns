from pydantic import BaseModel

class CreatePost(BaseModel):
    genre_id: int
    food_id: int

