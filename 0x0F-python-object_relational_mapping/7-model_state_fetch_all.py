#!/usr/bin/python3
"""Module to print the values of State"""
import sqlalchemy
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost:/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]), pool_pre_ping=True
    )

    Session = sessionmaker(engine)
    session = Session()
    consulta = session.query(State).all()

    for i in range(len(consulta)):
        print ("{}: ".format(consulta[i].__dict__['id']), end='')
        print ("{}".format(consulta[i].__dict__['name']))
