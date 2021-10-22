import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tdm_media.imdb import IMDB
import pandas as pd

def main():

    dat = IMDB("/depot/datamine/data/movies_and_tv/imdb.db")
    #9
    print(dat.kenneth_cox('nm0721526','Short',0))
    
    #66
    print(dat.kenneth_cox('nm0001877','Documentary',0))
    
    #1
    print(dat.kenneth_cox('nm3592338','Sci-Fi',6.8))

if __name__ == '__main__':
    main()