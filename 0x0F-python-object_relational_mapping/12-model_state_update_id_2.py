#!/usr/bin/env python3
"""
Module that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def change_state():
    """Change the name of a State object from the database hbtn_0e_6_usa
    """
    # get command line args
    [username, password, db_name] = sys.argv[1:]

    # initialize engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get state with id 2
    state = session.query(State).filter(State.id == 2).first()

    # change state name
    state.name = 'New Mexico'

    # commit changes
    session.commit()

    # close session
    session.close()


if __name__ == "__main__":
    change_state()
