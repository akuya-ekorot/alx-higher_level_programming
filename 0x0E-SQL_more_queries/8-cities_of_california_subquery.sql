-- lists all the cities of the state california in the db hbtn_0d_usa
-- results must be sorted in ascending order by cities.id
-- db name will be passed as an argument

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
