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
db.close()
