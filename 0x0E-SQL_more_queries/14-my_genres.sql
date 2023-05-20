-- lists all genres of the show Dexter
-- tv_shows table only has one record of Dexter
-- records should display tv_genres.name
-- use only on SELECT statement
-- db name will be passed as an argument

SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.name = 'Dexter';
