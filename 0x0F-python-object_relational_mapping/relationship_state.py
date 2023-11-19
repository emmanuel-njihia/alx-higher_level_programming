#!/usr/bin/python3
"""
Defines State model.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """state for a MySQL database.

    Attributes:
        __tablename__ : The name of the MySQL table.
        id : The state's id.
        name : The state's name.
        cities: The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
