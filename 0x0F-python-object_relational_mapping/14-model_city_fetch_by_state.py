#!/usr/bin/env python3
"""Module that prints all City object from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Main method that catches the arguments and
    make the query to the database
    """
    # get command line arguments
    [username, password, db_name] = argv[1:]

    # create engine to db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # make query
    query = session.query(City, State).filter(City.state_id == State.id).all()

    # print query
    for city, state in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == '__main__':
    main()
