import numpy as np
import FOBJ

def PART(X,PBEST):
    rows = len(X)
    cols = len(X[0])
    YCAL=FOBJ.OBJ(PBEST)
    NEW=FOBJ.OBJ(X).min()
    for i in range(rows):
        for j in range(cols):
            if(YCAL[i]>NEW):
                PBEST[i,j]=X[i,j]
    return PBEST