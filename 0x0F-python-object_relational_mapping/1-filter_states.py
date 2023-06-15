#!/usr/bin/env python3

import sys
import MySQLdb

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
