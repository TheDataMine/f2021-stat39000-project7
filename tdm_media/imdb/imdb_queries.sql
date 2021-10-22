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

-- name: Maxwell_Low_01$
-- Get the title of the movie/tv/episode/short with the given person_id and above a minimum rating
SELECT titles.primary_title FROM titles,crew,ratings WHERE titles.title_id = crew.title_id and titles.title_id = ratings.title_id and crew.person_id = :person_id and ratings.rating > :minimum_rating

-- name: robert_sego_01
-- Get avg ratings of episodes given title id of show
SELECT 
    AVG(ratings.rating) 
FROM ratings 
WHERE title_id in(
    SELECT 
        episode_title_id FROM episodes
    WHERE
        show_title_id = :title_id);
        
-- name: elise_miller_01
-- Get number of projects for a given name of an actor (person_name)

SELECT 
    COUNT(titles.title_id)
FROM titles, people, crew
WHERE people.name = :person_name AND crew.person_id = people.person_id AND titles.title_id = crew.title_id

-- name: kenneth_cox_01
-- Get number of projects for a given actor id, genre, and is greater than or equal to the minimum rating
SELECT
    COUNT(titles.title_id)
FROM titles, crew, ratings
WHERE crew.person_id = :person_id AND titles.title_id = crew.title_id AND ratings.rating > :miniumum_rating AND titles.title_id = ratings.title_id AND titles.genres LIKE :genre;

--name: aidan_kaczanowski_01
-- Get the number of titles in common between 2 actors
select 
  count(distinct a.title_id)
from 
(
  select title_id from crew
  left join people
    on people.person_id = crew.person_id
  where name = :person1
) as a
inner join
(
  select title_id from crew
  left join people
    on people.person_id = crew.person_id
  where name = :person2
) as b
on a.title_id = b.title_id

-- name: darren_iyer_01$
-- Get the birth year for the given person id
SELECT born FROM people WHERE person_id = :person_id;

-- name: darren_iyer_02$
-- Get the death year for the given person id
SELECT died FROM people WHERE person_id = :person_id;

-- name: darren_iyer_03$
-- Get the number of tv series which aired between the given years
SELECT COUNT(*) FROM (
    SELECT * FROM titles WHERE type = 'tvSeries' limit 1000
) tv
WHERE premiered > :born AND ended < :died;
