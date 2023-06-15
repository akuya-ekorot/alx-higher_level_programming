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
db.close()
