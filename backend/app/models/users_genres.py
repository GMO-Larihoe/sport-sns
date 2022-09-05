from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from database import Base

import models.users


class UserGenre(Base):
    __tablename__ = "users_genres"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(models.users.User.id), nullable=False, index=True)
    name = Column(String(64), nullable=False, index=True)
    
    def __init__(self, user_id: int, name: str):
        self.name = name
        self.user_id = user_id

        
    def toDict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name
        }

