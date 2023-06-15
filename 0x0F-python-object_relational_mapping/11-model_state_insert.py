#!/usr/bin/env python3
"""Fetch all from tables in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
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

    # create new record
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print record id
    print(new_state.id)

    # close session
    session.close()
