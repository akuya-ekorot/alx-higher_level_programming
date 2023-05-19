-- lists all records with a score >= 10 in the table second_table
-- results should be ordered
-- results should display both score and the name (in this order)

SELECT name,score
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
