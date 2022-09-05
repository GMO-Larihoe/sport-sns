from sqlalchemy import Column, Integer, String, SmallInteger
from database import Base

class UserStatus:
    Active = 1

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False, index=True)
    email = Column(String(64), nullable=False, unique=True, index=True)
    hashed_password = Column(String(128), nullable=False)
    status = Column(SmallInteger, nullable=False, index=True)
    
    def __init__(self, name: str, email: str, hashed_password: str):
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.status = UserStatus.Active
        
    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'hashed_password': self.hashed_password,
            'status': self.status
        }

