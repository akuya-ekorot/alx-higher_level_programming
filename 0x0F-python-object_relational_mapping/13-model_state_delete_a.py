#!/usr/bin/env python3
""" Module that deletes all State objects with a name containing the letter
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states():
    """ Deletes all State objects with a name containing the letter a from the
    database hbtn_0e_6_usa
    """
    # initialize the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete all State objects with a name containing the letter a
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()


# only run if not imported
if __name__ == '__main__':
    delete_states()
