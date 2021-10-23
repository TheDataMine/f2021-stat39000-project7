-- name: get_rating$
-- Get the rating of the movie/tv episode/short with the given id
SELECT rating FROM ratings WHERE title_id = :title_id;

-- name: kevin_amstutz_01
-- Get a list of episode names given the title id of the show
SELECT
	primary_title
FROM
	titles
WHERE
	title_id in(
		SELECT
			episode_title_id FROM episodes
		WHERE
			show_title_id = :title_id);
            
-- name: Justin_Mathew_01$
-- Get the rating of the movie/tv episode/short with the given id
SELECT AVG(ratings.rating) FROM ratings,crew,titles WHERE crew.title_id = titles.title_id and ratings.title_id = titles.title_id and crew.person_id = :person_id

-- name: trevor_teague_01$
-- Get the number of seasons for a show with given id 
SELECT MAX(season_number) from episodes WHERE show_title_id= :title_id