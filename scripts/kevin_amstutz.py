import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd


def main():
    
    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    print(dat.kevin_amstutz("tt5180504"))

    print(dat.kevin_amstutz("tt0332280"))

if __name__ == '__main__':
    main()