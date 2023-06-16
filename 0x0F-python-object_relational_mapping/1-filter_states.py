#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

import sys
import MySQLdb


# function to filter states
def filter_states(db):
    """filters states that start with 'N'"""

    # create cursor
    cur = db.cursor()
    query = """
    SELECT id, name
    FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC;
    """

    # execute command
    cur.execute(query)
    filtered_states = cur.fetchall()

    # print results
    for state in filtered_states:
        print(state)


if __name__ == "__main__":
    # get command line arguments
    username, password, db_name = sys.argv[1:]

    # create db
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name
    )

    # filter states
    filter_states(db)

    # close cursor and database
    db.close()
