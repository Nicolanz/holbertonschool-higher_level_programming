#!/usr/bin/python3
"""Module of model state"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)

Base = declarative_base()


class State(Base):
    """Class State

    Args:
        Base ([base]): [Base class]
    """
    __tablename__ = 'states'

    id = sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True
    )
    name = sqlalchemy.Column(
        'name',
        sqlalchemy.String(128),
        nullable=False
    )
