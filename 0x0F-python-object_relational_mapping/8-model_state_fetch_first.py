#!/usr/bin/python3
"""Module to list the first State object"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()
    try:
        consulta = session.query(State).get(1)
        print("{}: {}".format(
            consulta.__dict__['id'],
            consulta.__dict__['name'])
        )
    except:
        print()
