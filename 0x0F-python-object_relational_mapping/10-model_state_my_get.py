#!/usr/bin/python3
"""Module to print the State which contain an a"""

import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]), pool_pre_ping=True
    )

    Session = sessionmaker(engine)
    session = Session()
    consulta = session.query(State).all()

    for i in range(len(consulta)):
        if (consulta[i].__dict__['name'] == sys.argv[4]):
            print(consulta[i].__dict__['id'])
            break
        elif (i+1 == len(consulta) and consulta[i].__dict__['\
        name'] is not sys.argv[4]):
            print("Not found")
            break
        else:
            continue
