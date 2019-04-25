# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 6
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#

from numpy import *
from math  import factorial
from numpy.linalg import solve
eps = finfo('float').eps



def doublePrime(alpha):
    h=0.5
    n=len(alpha)
    
    for i in range(n):
        alpha[i]= float(alpha[i])
    
    print("alpha= ",alpha)
    print("n= ",n)
    
    factor = sum([alpha[i] * (h/factorial(n+1)) for i in range(n)])
    order = n+1
    print("factor= ",factor)
  
    beta = zeros(n)
    b= zeros(n)
    b[1]=1
    rangelist= [i for i in range(0,n)]
    del rangelist[1]
    print("rangelist= ",rangelist)
    Acolonne= [ -(2*h**(i)) / (factorial(i)*h**2) for i in range(1,n+1)]
    print("Acolonne= ",Acolonne)
    A=[ [0 for i in range(n)] for j in range(n)]
    print()
    print("A= ",A)
    for i in rangelist:
        print("multiple de a= ",Acolonne[i])
        for j in range(0,n):
            print("i= ",i,"  alpha[j]= ",alpha[j])
            if alpha[j] != 0 :
                A[i][j]= Acolonne[i] * alpha[j]**(i-2)
            else:
                A[i][j]= -2/factorial(i+1)
        print("Aline%s= "%i,A[i])
        
    print()
    A[1]= [1 for i in range(n)]
    print("A= ",A)
    print("b= ",b)
    beta=linalg.solve(A,b)
    print("beta avt *2/(a*h)**2= ",beta)
    beta2= zeros(n)
    for i in range(n):
        if alpha[i] != 0:
            beta2[i]= 2*beta[i]/ ( (alpha[i]*h)**2 )
        else:
            ialpha0= i
    beta2[ialpha0]= -2*(sum(beta[i])-beta[ialpha0]) / ( (alpha[i]*h)**2 )
            
    print("beta2= ",beta2)

    
  

    
    return beta,factor,order

doublePrime([-1,0,2])