#!/usr/bin/python3
"""Module to list all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


# function to get all cities by state
def get_cities_by_state(db):
    """Function to list all cities from the database hbtn_0e_4_usa
    """
    # create cursor
    cur = db.cursor()

    # craft query
    query = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    # execute and fetch query
    cur.execute(query, (filter,))
    results = cur.fetchall()

    # print results
    city_names = [city[0] for city in results]
    print(', '.join(city_names))

    # close the cursor and db
    cur.close()


if __name__ == "__main__":
    # get command line arguments
    username, password, db_name, filter = sys.argv[1:5]

    # create db
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name)

    # get all cities by state
    get_cities_by_state(db)

    # close db
    db.close()
