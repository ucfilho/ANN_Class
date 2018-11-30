
"""
Created on Fri Dec 06 2017
@author: ucfilho
"""
import numpy as np
import pandas as pd
import FOBJ
import ENX
import VEL
import PART
import GBEST


def PSO(W,C1,C2,NPAR,ITE,PAR,MAX,MIN):
    # INICIALIZA O METODO-
    X=ENX.Enxame(PAR,NPAR,MAX,MIN) # CRIA A POPULACAO
    ycal=FOBJ.OBJ(X) # CALCULA A FUNCAO OBJETIVO PARA TODAS PARTICULAS
    PBEST=PART.PART(X,X) # O MELHOR LOCAL DE CADA PARTICULA INICIALMENTE ALEATORIA
    BEST=[]
    for i in range(PAR):
        BEST.append(1e10)
    BEST=GBEST.BEST(X,BEST)
    VELOC=ENX.Enxame(PAR,NPAR,MAX,MIN)# VELOCIDADES INICIALMENTE ALEATORIAS
    RESP=[]
    for k in range(ITE):
        yteste=FOBJ.VALOR(BEST)
        VELOC, X=VEL.VE(X,VELOC,BEST,PBEST,W,C1,C2)
        BEST=GBEST.BEST(X,BEST)
        PBEST=PART.PART(X,PBEST)
        yteste=FOBJ.VALOR(BEST)
        RESP.append(yteste)
    return RESP
