from typing import List
from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    
    
class UserBase(BaseModel):
    email: EmailStr
    name: str

class User(UserBase):
    id: int
    status: int

    class Config:
        orm_mode = True

class CreateUser(UserBase):
    hashed_password: str

class UserScore(BaseModel):
    name: str
    score: int
    
    class Config:
        orm_mode = True
