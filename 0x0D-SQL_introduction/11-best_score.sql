-- Lists all records in the table
-- Rrcords are ordered by descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
