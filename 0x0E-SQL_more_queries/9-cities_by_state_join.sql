-- lists all cities contained in the database
-- each record should display cities.id, cities.name and states.name
-- ordered in ascending order by cities.id
-- only use one select statement
-- db name will be passed as an argument

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = state.id
ORDER BY cities.id;
