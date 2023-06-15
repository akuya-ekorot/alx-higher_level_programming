#!/usr/bin/env python3

import sys
import MySQLdb

# get command line arguments
username, password, db_name, filter = sys.argv[1:]

# create db
db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name)

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
