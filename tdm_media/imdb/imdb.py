"""
This module is intended to be used to mess around with movie and tv data from imdb.
This module is intended to be used and developed on by students in Purdue Universities The Data Mine.
"""


import os
import aiosql
import sqlite3
import pandas as pd
from pathlib import Path
from typing import Tuple


class IMDB:
    def __init__(self, db_path: str):
        self._db_path = Path(db_path)
        self.queries = aiosql.from_path(Path(__file__).parents[0] / "imdb_queries.sql", "sqlite3")
    

    def __str__(self):
        return f'IMDB data from: {self._db_path}'


    def get_rating(self, title_id: str) -> float:
        """
        Given an IMDB `title_id`, return the rating for the corresponding episode,
        movie, short, etc.

        Args:
            title_id (str): The IMDB title id.

        Returns:
            float: The numeric rating of the corresponding episode, movie, short, etc.
        """
        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the rating
        rating = self.queries.get_rating(conn, title_id = title_id)

        # close the database connection
        conn.close()

        return rating
    
    def nicolas_newman(self, language: str) -> float:
        """
        Given an IMDB `language`, calculate the average raiting of all titles in that language
        
        Args:
            language (str): The IMDB language code
            
        Returns:
            float: the average raiting for all titles in the specified language
        """
        conn = sqlite3.connect(self._db_path)
        raiting = self.queries.nicolas_newman_01(conn, language = language)
        conn.close()
        return raiting
    
    def Maxwell_Low(self, person_id: str, minimum_rating: float) -> str:
        """
        Given an IMDB `person-Id`, and a minimum rating,
        return all titles that contain that person and are above the minimum rating

        Args:
            person_id (str): The IMDB person id

        Returns:
            str: The list of titles which contain the corresponding person and all episode, movie, short, etc they appeared in above a particular minimum rating
        """
        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the rating
        titles = self.queries.Maxwell_Low_01(conn, person_id = person_id, minimum_rating = minimum_rating)

        # close the database connection
        conn.close()

        return titles
    
    def robert_sego(self, title_id: str) -> float:
        """
        Given an IMDB 'title_id', return average rating for all episodes, movies, 
        shorts, etc.
        
        Args:
            title_id (str): The IMDB title id.
        
        Returns:
            float: Numeric average rating for all media with corresponding title
        
        """
        # establish a database connection
        conn = sqlite3.connect(self._db_path)
        
        # get average rating of show
        avg_rating = self.queries.robert_sego_01(conn, title_id=title_id)
        
        # close database connection
        conn.close()
        
        return avg_rating
    
    def Justin_Mathew(self, person_id: str) -> float:
        """
        Given an IMDB `person_id`, return the average rating for the corresponding in all episode, movie, short, etc they have appeared in.

        Args:
            person_id (str): The IMDB person id.

        Returns:
            float: The numeric average rating for the corresponding person in IMDB.
        """
        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the rating
        rating = self.queries.Justin_Mathew_01(conn, person_id = person_id)

        # close the database connection
        conn.close()

        return rating
    
    def kenneth_cox(self, person_id: str, genre: str, miniumum_rating: float) -> int:
        """
        Given an IMDB `person_id`, project genre, and the projects miniumum 
        rating it returns the total number of movies, episodes, series, 
        shorts etc. that the person has appeared in with that genre.
        
        Args:
            person_id (str): IMDB person id
            genre(str): the genre that the projects must be a part of
            minimum_rating(int): the minimum rating the project must have
            
        Returns:
            int: the number of movies, episodes, series, shorts etc. that the person has appeared in with that genre.
        """
        # establish a database connection
        conn = sqlite3.connect(self._db_path)
        
        # get the number of projects that the actor was in meeting the given critera
        number = self.queries.kenneth_cox_01(conn, person_id = person_id, genre = '%' + genre + '%', miniumum_rating = miniumum_rating)
        
        #close the database connection
        conn.close()
        
        return number[0][0]
    
    def kevin_amstutz(self, title_id: str) -> Tuple[str]: 
        """
        Given an IMDB `title_id`, return names of the episodes, or
        raise a ValueError if the title id doesn't have episodes.

        Args:
            title_id (str): The IMDB title id.

        Raises:
            ValueError: If the `title_id` does not have an episode.

        Returns:
            Tuple[str]: A tuple with episode names.
        """

        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the rating
        episodes = self.queries.kevin_amstutz_01(conn, title_id = title_id)
        episodes = tuple(e[0] for e in episodes)

        # close the database connection
        conn.close()

        # make sure the title_id has episodes, raise ValueError otherwise.
        if not episodes:
            raise ValueError(f"title_id: {title_id} does not contain episodes.")

        return episodes
    
    
    def elise_miller(self, person_name:str) -> int:
        
        """
        Given an IMDB actor name, return the number of projects they have been involved in. 
        Counted by titles.title_id.

        Args:
            person_name (str): The actor name.


        Returns:
            int: The number of projects the actor has been involved in.
        """
            
        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the rating
        value = self.queries.elise_miller_01(conn, person_name = person_name)

        # close the database connection
        conn.close()
        
        return value[0][0]
    
    def ben_moorman(self, person_1: str, person_2: str) -> int:
        """
        Given two IMDB `person_id`, return the number of projects where both
        people worked together on the project.

        Args:
            person_1 (str): Name of first person
            person_2 (str): Name of second person

        Raises:
            ValueError: If names person_1 or person_2 cannot be matched to a person_id.

        Returns:
            int: the number of projects where person_1 and person_2 worked together
        """
        
        conn = sqlite3.connect(self._db_path)
        
        person1_id = self.queries.ben_moorman_01(conn, person=person_1)
        person2_id = self.queries.ben_moorman_01(conn, person=person_2)
        
        # make sure the title_id has episodes, raise ValueError otherwise.
        if not person1_id:
            raise ValueError(f"person_1: {person_1} cannot be found.")
        else: person1_id = person1_id[0]

        if not person2_id:
            raise ValueError(f"person_2: {person_2} cannot be found.")
        else: person2_id = person2_id[0]
        
        person1_id = person1_id[0]
        person2_id = person2_id[0]
        
        value = self.queries.ben_moorman_02(conn, person1_id = person1_id, person2_id = person2_id)

        # Close the database connection
        conn.close()
        
        return value[0][0]

    def aidan_kaczanowski(self, person1:str, person2:str) -> int:
        """
        Given the names of two IMDB actors, return the number of projects they worked
        together on.

        Args:
            person1 (str): The name of the first actor
            person2 (str): The name of the second actor
        Returns:
            int: The number of projects common between the two actors.
        """
        
        # establish a database connection
        conn = sqlite3.connect(self._db_path)

        # get the number
        value = self.queries.aidan_kaczanowski_01(conn, person1 = person1, person2 = person2)
        
        # close the database connection
        conn.close()

        return value[0][0]
    
    def darren_iyer(self, person_id: str) -> int:
        '''
        Given a person's id, return the number of tv series that premiered
        and ended in the span of the person's life. (The series started and 
        ended within the person's lifespan)
        
        Args:
            person_id (str): The person's id
        
        Raises:
            ValueError: If the person is still alive
        
        Returns:
            int: The number of tv series which aired in the span of the person
        '''
        
        # establish connection
        conn = sqlite3.connect(self._db_path)

        # get the person tuple
        born = self.queries.darren_iyer_01(conn, person_id = person_id)
        died = self.queries.darren_iyer_02(conn, person_id = person_id)
        
        if died is None:
            raise ValueError(f"person_id: {person_id} is still alive")
        
        # get the count of tv series
        num = self.queries.darren_iyer_03(conn, born = born, died = died)
        
        conn.close()
        
        return num

if __name__ == '__main__':
    import doctest
    doctest.testmod()
