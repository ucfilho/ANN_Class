'''
Certos problemas a funcao objetivo e a propria funcao em estudo
outros problemas nao segue esta logica por isto usaremos um arquivo
FOBJ.py no lugar de apenas um arquivo de funcoes...
'''

import FUN
import numpy as np


def OBJ(x):
    rows = len(x)
    cols = len(x[0])
    fobj=np.zeros(rows)
    for i in range(rows):
        for j in range(cols):
            fobj[i]=FUN.Rosenbrock(x[i,])
    return fobj
    # return fobj.min()

def VALOR(x):
    fob=FUN.Rosenbrock(x)
    return fob

