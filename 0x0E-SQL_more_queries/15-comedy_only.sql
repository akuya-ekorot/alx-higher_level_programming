-- lists all comedy shows in the db
-- tv_genres has only one record of 'Comedy'
-- record should display tv_shows.title
-- sort in ascending order by the show title
-- only use on SELECT statement
-- db name will be passed as an argument

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy';
