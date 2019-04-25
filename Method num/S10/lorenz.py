# -------------------------------------------------------------------------
# PYTHON for DUMMIES 18-19
# Problème 7
# -------------------------------------------------------------------------


from numpy import *


  
def lorenz(Xstart,Xend,Ustart,n):
    X = linspace(Xstart,Xend,n+1)
    h= (Xend - Xstart) / n
    
    def f(arg):
        x,y,z= arg
        return array(((10*y-10*x),(28*x-y-x*z),(x*y-(8/3)*z)))
        
    U= zeros( (n,3) )
    U[0]= (0,1,0)
    for i in range(1,n):
        K_1= f( U[i-1] )
        K_2= f(U[i-1] + (h/2)*K_1)
        K_3= f(U[i-1] + (h/2)*K_2)
        K_4= f(U[i-1] + h*K_3)
        U[i]= U[i-1] + (h/6)*(K_1 + 2*K_2 + 2*K_3 + K_4)
    
    return X,U


