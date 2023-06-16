#!/usr/bin/python3
"""Create a class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class definition of a City
    Args:
        Base (class): base class from which to inherit

    Attributes:
        id (int): unique identifier
        name (str): name of city
        state_id (int): id of state
    """
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
