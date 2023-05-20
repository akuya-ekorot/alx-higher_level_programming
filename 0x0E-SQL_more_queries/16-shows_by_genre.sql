-- list all shows and all genres linked to that show from the db
-- each record should display tv_shows.title, tv_genres.name
-- ascending order by the show title and genre name
-- one select statement
-- db will be passed as an argument

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
