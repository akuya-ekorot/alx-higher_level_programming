-- lists all shows in the db
-- display tv_shows.title, tv_show_genres.genre_id
-- order by tv_shows.title and tv_show_genres.genre_id
-- if show doesn't have a genre display NULL
-- use only on SELECT statement
-- db name will be passed as an argument

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_show.id
ORDER BY tv_shows.title, tv_show_genre.genre_id;
