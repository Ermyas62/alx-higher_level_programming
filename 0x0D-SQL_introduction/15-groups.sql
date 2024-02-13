-- Lists all number of records with the same score
-- Records are ordered by descending counts
SELECT `score`, COUNT(*) AS `number`
from `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
