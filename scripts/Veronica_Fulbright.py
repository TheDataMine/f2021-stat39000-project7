import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():

    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    # code to use your method here, for example:
    print(dat.veronica_fulbright("tt0347149"))
    
    print(dat.veronica_fulbright("tt12063450"))

if __name__ == '__main__':
    main()