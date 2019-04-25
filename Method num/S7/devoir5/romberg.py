# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 5
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#

from numpy import *

#
# TOUTE AUTRE INSTRUCTION CONTENANT import / from SERA AUTOMATIQUEMENT SUPPRIMEE
#

def trapezeEasy(f,a,b,n):
    hdemi= ( (b-a)/n )/2
    X= linspace(a,b,n+1)
    U= f(X)
    I= sum(2*U) - U[0] - U[n]
    return I * hdemi
  
def romberg(f,a,b,n,nmax,tol,i=0,j=0):
    list=[[trapezeEasy(f,a,b,1)],[trapezeEasy(f,a,b,2)]]
    coef=4
    list[-1].append( (coef*list[1][0]-list[0][0]) / (coef-1) )
    i=1
    while abs(list[-1][-1] - list[-1][-2]) > tol and 2**(i+1) < nmax:
        i+=1
        list.append([trapezeEasy(f,a,b,2**i)])
        for j in range(1,len(list[-2])+1):
            coef= 2**(2*j)
            list[-1].append( (coef*list[i][j-1]-list[i-1][j-1]) / (coef-1) )
    
    I= list[-1][-1]
    errorEst= abs(I-list[-1][-2])
    n=2**i
    printlist(list)
    return I,n,errorEst
  
def printlist(list):
    for row in list:
        print(row)
