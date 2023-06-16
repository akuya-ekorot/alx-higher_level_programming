#!/usr/bin/python3
"""Fetch all from tables in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # initialize engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # build query and execute
    query = session.query(State)
    results = query.filter(State.name.contains('a'))

    # print results
    for result in results:
        print("{}: {}".format(result.id, result.name))

    # close session
    session.close()
