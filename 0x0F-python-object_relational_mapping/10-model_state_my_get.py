#!/usr/bin/env python3
"""Fetch all from tables in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # get command line args
    [username, password, db_name, search_term] = sys.argv[1:]

    # initialize engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # build query and execute
    query = session.query(State)
    result = query.filter_by(name=search_term).first()

    # print results
    if result:
        print("{}".format(result.id))
    else:
        print('Not found')

    # close session
    session.close()
