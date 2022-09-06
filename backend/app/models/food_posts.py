from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime, date
from database import Base

import models.users_genres
import models.users
import models.foods


class FoodPost(Base):
    __tablename__ = "food_posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(models.users.User.id),  nullable=False, index=True)
    genre_id = Column(Integer, ForeignKey(models.users_genres.UserGenre.id), nullable=False, index=True)
    food_id = Column(Integer, ForeignKey(models.foods.Food.id), nullable=False, index=True)
    date = Column(Timestamp, nullable=False, server_default=current_timestamp())

    
    def __init__(self, user_id: int, genre_id: int, food_id: int, date: datetime):
        self.user_id = user_id
        self.genre_id = genre_id
        self.food_id = food_id
        self.date = date



        
    def toDict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'genre_id': self.genre_id,
            'food_id': self.food_id,
            'date': self.date
        }

