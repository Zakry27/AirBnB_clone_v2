#!/usr/bin/python3
"""the city class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """class for City

    Attributes:
        state_id: state id
        name: input name
        places (sqlalchemy relationship): user-Place relationship.
    """

    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ''
        name = ''
