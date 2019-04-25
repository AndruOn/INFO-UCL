

from numpy import *
from scipy.interpolate import CubicSpline as spline


def hermite(x,X,U,dU):
    
    i = zeros(len(x),dtype=int)
    for j in range(1,len(X)-1):
        i[X[j]<=x] = j

    uh= empty(len(x))
    for index in range(len(x)):
        h=X[i[index]+1] - X[i[index]]
        s=  x[index] - X[i[index]]
        uh[index]= U[i[index]+1]*(3*h*(s**2)-2*(s**3))/h**3 + U[i[index]]*(h**3-3*h*(s**2)+2*(s**3))/h**3+ dU[i[index]+1]*(s**2)*(s-h)/h**2 + dU[i[index]]*s*((s-h)**2)/h**2

    return uh


  
