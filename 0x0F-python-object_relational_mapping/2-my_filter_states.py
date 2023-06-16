#!/usr/bin/python3
"""Lists states from the database hbtn_0e_0_usa based on user input"""

import sys
import MySQLdb


# function to list states
def list_states(db, username, password, db_name, filter):
    """Lists states from the database hbtn_0e_0_usa based on user input"""

    # create cursor
    cur = db.cursor()

    # craft query
    query = """
    SELECT id, name
    FROM states
    WHERE name = '{}'
    ORDER BY id ASC;
    """.format(filter)

    # execute and fetch query
    cur.execute(query)
    results = cur.fetchall()

    for result in results:
        print(result)

    # close cursor
    cur.close()


if __name__ == "__main__":
    # get command line arguments
    username, password, db_name, filter = sys.argv[1:]

    # create db
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name)

    # list states
    list_states(db, username, password, db_name, filter)

    # close db
    db.close()
