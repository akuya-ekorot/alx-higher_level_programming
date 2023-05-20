-- lists all shows contained in the hbtn_0d_tvshows db
-- each record should display tv_shows.title, tv_shows_genres.genre_id
-- Ordered in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Use only one SELECT statement
-- db name will be passed as an argument

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
