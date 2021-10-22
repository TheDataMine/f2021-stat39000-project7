import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB


def main():
    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")

    print(dat.aidan_kaczanowski("John O'Keefe", "Joey Silvera"))

if __name__ == '__main__':
    main()
