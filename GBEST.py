import numpy as np
import FOBJ

def BEST(X,BEST):
    rows = len(X)
    cols = len(X[0])
    YCAL=FOBJ.OBJ(X)
    NEW=FOBJ.VALOR(BEST)
    for i in range(rows):
        for j in range(cols):
            if(YCAL[i]<NEW):
                NEW=YCAL[i]
                BEST[j]=X[i,j]
    return BEST