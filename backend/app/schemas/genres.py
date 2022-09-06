from pydantic import BaseModel

class Genre(BaseModel):
    id: int
    user_id: int
    name: str

    class Config:
        orm_mode = True