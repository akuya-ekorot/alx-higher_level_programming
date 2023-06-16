#!/usr/bin/python3
"""Module to list all cities with their states from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


# function to get cities by state
def get_cities_by_state(db):
    """Function to list all cities with their states from the database
    """
    # create cursor
    cur = db.cursor()

    # craft query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """

    # execute and fetch query
    cur.execute(query)
    results = cur.fetchall()

    # print results
    for result in results:
        print(result)

    # close the cursor
    cur.close()


if __name__ == '__main__':
    # get command line arguments
    username, password, db_name = sys.argv[1:]

    # connect to database
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name)

    # call function to get cities by state
    get_cities_by_state(db)

    # close database
    db.close()
