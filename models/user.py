#!/usr/bin/python3
"""The user class"""
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """A class representing a user in a system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
