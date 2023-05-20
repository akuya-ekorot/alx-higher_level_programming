-- lists all genres from db and displays the number of shows linked to each
-- display tv_show_genres.name, number of shows linked to this genre
-- first column must be called genre
-- second column must be called number_of_shows
-- don't display a genre that doesn't have any shows linked
-- only use one SELECT statement
-- db name will be passed as an argument

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre;
