from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.mysql import DATE as Date
from sqlalchemy.sql.functions import current_date
from datetime import datetime, date
from database import Base

import models.users


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(models.users.User.id), nullable=False, index=True)
    score = Column(Integer, nullable=False)
    date = Column(Date, nullable=False, server_default=current_date)

    
    def __init__(self, user_id: int, score: int, date: date):
        self.user_id = user_id
        self.score = score
        self.date = date


        
    def toDict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'score': self.score,
            'date': self.date
        }

