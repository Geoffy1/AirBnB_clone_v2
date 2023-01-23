#!/usr/bin/python3
""" State Module for HBNB proj """
from os import getenv
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """ getter attr for file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
