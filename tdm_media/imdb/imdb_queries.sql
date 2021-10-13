-- name: get_rating$
-- Get the rating of the movie/tv episode/short with the given id
SELECT rating FROM ratings WHERE title_id = :title_id;