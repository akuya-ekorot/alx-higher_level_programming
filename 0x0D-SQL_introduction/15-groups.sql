-- lists the number of records with the same score in second_table
-- results should display score, number of records for this score with the label number
-- sorted by the number of recordds (descending)

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
