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

    
    def kevin_amstutz(self, title_id: str) -> Tuple[str]: 
        """
        Given an IMDB `title_id`, return names of the episodes, or
        raise a ValueError if the title id doesn't have episodes.

        Args:
            title_id (str): The IMDB title id.

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

        return episodes


if __name__ == '__main__':
    import doctest
    doctest.testmod()
