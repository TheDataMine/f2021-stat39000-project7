import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():

    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    # code to use your method here, for example:
    #getting the highest rated titles from 1990, because it's a short list
    print(dat.laura_humphrey(1990, 9.9))

if __name__ == '__main__':
    main()
