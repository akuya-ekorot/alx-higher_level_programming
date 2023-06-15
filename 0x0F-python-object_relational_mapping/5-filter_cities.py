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
db.close()
