import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }

class CategoryItem(Base):
    __tablename__ = 'category_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(800))  
    url_image = Column(String(800)) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    categories_id = Column(Integer, ForeignKey('categories.id'))   
    categories = relationship(Categories)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
			'url_image': self.url_image,
            'id': self.id,
        }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
