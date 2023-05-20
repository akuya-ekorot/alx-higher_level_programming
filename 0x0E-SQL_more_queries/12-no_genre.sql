-- lists all shows contained in the db without a genre linked
-- each record should display tv_shows.title, tv_show_genres.genre_id
-- results are ordered in ascending order by tv_shows.title and tv_show_genres.genre_id
-- use only one SELECT statement
-- db name will be passed as an argument

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL;
