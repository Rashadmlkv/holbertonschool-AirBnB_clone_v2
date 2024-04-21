#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    def __init__(self, *args, **kwargs):
        """ Initialization of State instance """
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter Function for FileStorage"""
            from models import storage
            result = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    result.append(city)
            return result
