import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():

    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    print(dat.robert_sego("tt5180504"))

    print(dat.robert_sego("tt0332280"))
    
    print(dat.robert_sego("tt7745956"))

if __name__ == '__main__':
    main()