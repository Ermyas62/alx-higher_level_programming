-- Lists all cities of CA
-- Results are ordered by asciending cities.id
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
	(SELECT `id`
		FROM `states`
		WHERE `name` = "California")
ORDER BY `id`;
