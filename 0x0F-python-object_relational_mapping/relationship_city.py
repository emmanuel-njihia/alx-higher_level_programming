#!/usr/bin/python3

"""
Defines a City model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """city for a MySQL database.

    Attributes:
        id : The city's id.
        name : The city's name.
        state_id: The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
