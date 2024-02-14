-- Lists all shows that have at least one gener
-- Records are sorted by ascending tv_shows.title
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv.shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
