-- Lists all comedy shows
-- Records are ordered by descending show title
SELECT title FROM tv_shows
JOIN tv_show_genres ON id = tv_show_genres.genre_id
JOIN tv-genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
