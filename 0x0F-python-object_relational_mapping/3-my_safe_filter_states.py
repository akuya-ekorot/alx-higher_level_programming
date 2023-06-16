#!/usr/bin/python3
"""Module to filter states by user input"""

import sys
import MySQLdb


# function to filter by user input
def filter_states(db):
    """Filter states by user input"""
    # create cursor
    cur = db.cursor()

    # craft query
    query = """
    SELECT id, name
    FROM states
    WHERE name = %s
    ORDER BY id ASC;
    """

    # execute and fetch query
    cur.execute(query, (filter,))
    results = cur.fetchall()

    # print results
    for result in results:
        print(result)

    # close the cursor
    cur.close()


if __name__ == '__main__':
    # get command line arguments
    username, password, db_name, filter = sys.argv[1:]

    # create db
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name)

    filter_states(db)
    db.close()
