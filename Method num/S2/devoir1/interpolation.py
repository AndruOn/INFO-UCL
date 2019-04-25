

from numpy import *
from numpy.linalg import solve



x = linspace(-100,100,201)

def interpolation(X,U,x):
    n= len(X)//2
    matrice_exp=[]
    for x_i in X:
        matrice_exp.append(  exp( [(-n+i)*1j*x_i for i in range(2*n+1)] )  )
    
    a_k= solve(matrice_exp,U)
    print("a= ",a_k)
    def f(a_k,x):
        sum=0
        for i in range(len(a_k)):
            sum+= a_k[i] * exp ((-n+i)*1j*x)
        return sum
    print("f(x)= ",f(a_k,x))
    return f(a_k,x)






uh= interpolation([0,1,2,3,4],[1,2,4,2,1],x)

