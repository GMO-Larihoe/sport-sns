from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

import models.users_genres


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True, index=True)
    genre_id = Column(Integer, ForeignKey(models.users_genres.UserGenre.id), nullable=False, index=True)
    name = Column(String(64), nullable=False, index=True)
    img = Column(Text, nullable=False)
    carbohydrate = Column(Integer, nullable=False)
    lipid = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    mineral = Column(Integer, nullable=False)
    vitamin = Column(Integer, nullable=False)

    
    def __init__(self, genre_id: int, name: str, img: str, carbohydrate: int, lipid: int, protein: int, mineral: int, vitamin: int):
        self.genre_id = genre_id
        self.name = name
        self.img = img
        self.carbohydrate = carbohydrate
        self.lipid = lipid
        self.protein = protein
        self.mineral = mineral
        self.vitamin = vitamin


        
    def toDict(self):
        return{
            'id': self.id,
            'genre_id': self.genre_id,
            'name': self.name,
            'img': self.img,
            'carbohydrate': self.carbohydrate,
            'lipid': self.lipid,
            'protein': self.protein,
            'mineral': self.mineral,
            'vitamin': self.vitamin
        }

