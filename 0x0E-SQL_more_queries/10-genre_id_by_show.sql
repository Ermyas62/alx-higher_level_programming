-- Lists all shows that have at least one gener
-- Records are sorted by ascending tv_shows.title
SELECT s.`title`, g.`genre_id`
FROM `tv.shows` AS s
	INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
