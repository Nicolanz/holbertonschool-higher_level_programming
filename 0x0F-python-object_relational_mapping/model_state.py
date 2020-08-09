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

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            ), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
