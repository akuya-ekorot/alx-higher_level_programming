-- lists all records of second_table
-- don't list rows without a name value
-- results should display the score and the name (in this order)
-- records should be listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
