# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 4
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#

from numpy import *



def trapezeEasy(f,a,b,n):
    hdemi= ( (b-a)/n )/2
    X= linspace(a,b,n+1)
    U= f(X)
    I= sum(2*U) - U[0] - U[n]
    return I * hdemi
   
  
def trapezeFun(f,a,b,n,nmax,tol):
    errorEst = 100
    next= trapezeEasy(f,a,b,n)
    while errorEst > tol and n*2 < nmax:
        n = n*2
        I= next
        next= trapezeEasy(f,a,b,2*n)
        errorEst= (next-I)
        
        
    return I,n,errorEst 
  

