from numpy import *
from numpy.linalg import solve




def spline(x,h,U):
    n = size(U); X = arange(0,n+1)*h
    i = zeros(len(x),dtype=int)
    for j in range(1,n):
        i[X[j]<=x] = j
   
    i= i+1
    
    A= [ [0 for i in range(n)] for i in range(n)]
    for j in range(0,n):
        A[j][j-1]=h/6
        A[j][(j)%n]=2*h/3
        A[j][(j+1)%n]=h/6
        
    b=[ ((U[(j+1)%n]-U[j%n])-(U[j%n]-U[(j-1)%n]))/h for j in range(n) ]
    
    ddU= linalg.solve(A,b)
    dif= X[i]-x
    cdif= x-X[i-1]
    print("A",A)
    print("b",b)
    print("ddU",ddU)
    return (ddU[(i-1)%n]*(dif**3)) / (6*h) + (ddU[i%n]*(cdif**3)) / (6*h) + (U[(i-1)%n]/h - ((ddU[(i-1)%n]*h)/6))*(dif) + (U[i%n]/h - ((ddU[i%n]*h)/6))*(cdif)

