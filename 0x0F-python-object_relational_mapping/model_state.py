#!/usr/bin/python3
"""Module of model state"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
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
