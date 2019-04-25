from numpy import *
from math  import factorial
from numpy.linalg import solve
eps = finfo('float').eps


def doublePrime(alpha):
    n = len(alpha) 

    b= zeros(n)
    b[2]= 2
    A = [power(alpha, i) for i in range(n)]
    beta= solve(A, b)
    
    gamma= factorial(n)*sum([1/(beta[i]*alpha[i]**n) for i in range(n)])
    order= n-2
    return beta,gamma,order
