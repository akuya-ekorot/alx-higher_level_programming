#!/usr/bin/python3
"""Module to create a class State and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance of declarative_base
Base = declarative_base()


class State(Base):
    """Class State that inherits from Base
    Args:
        Base: Instance of declarative_base
    Attributes:
        id: Integer column id that is primary key
        name: String column name
    """

    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)
