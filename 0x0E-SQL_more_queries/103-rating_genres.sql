-- List all genres in the database by their rarting
-- Records are ordered by descendeing rating
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS s
	ON s.`gener_id` = g.`id`

	INNER JOIN `tv_show_ratings` AS r
	ON r.`show_id` = s.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
