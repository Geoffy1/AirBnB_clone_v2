#!/usr/bin/python3
""" City Module for HBNB proj """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city cls, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
