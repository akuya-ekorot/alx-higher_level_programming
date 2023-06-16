#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb


# function to list all states from database
def list_all_states():
    """ Lists all states from database """

    # get command line arguments
    username, password, db_name = sys.argv[1:]

    # create db
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=db_name)

    # create cursor
    cur = db.cursor()

    # execute command
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    # print results
    for state in states:
        print(state)


if __name__ == '__main__':
    list_all_states()
