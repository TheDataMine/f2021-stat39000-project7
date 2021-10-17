import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():
    print(f'Pandas is here!: {pd.__file__}')
    print(f'^^^^^^^')
    print(f'If that doesnt start with something like "$HOME/f2021-stat39000-project7/.venv/..., you did something wrong')
    
    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")
    print(dat)

    print(dat.get_rating("tt5180504"))

if __name__ == '__main__':
    main()