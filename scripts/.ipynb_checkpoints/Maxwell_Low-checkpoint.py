import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():

    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    # code to use your method here, for example:
    # William Shatner
    print(dat.Maxwell_Low("nm0000638", 6))
    
    # Daniel Craig
    print(dat.Maxwell_Low("nm0185819", 8))

if __name__ == '__main__':
    main()