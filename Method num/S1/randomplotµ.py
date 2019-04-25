'''xi = x_i-1 + h'''
from numpy import *
import matplotlib.pyplot as plt



X = linspace(-1,1,7)
x = linspace(-1,1,1001)

def f(t):
    return prod(t-X)

y=list(map(f,x))
plt.plot(x,y)
plt.show()


a=[1,2,5,9]
a= array(a)
print(1-a)
print(prod(1-a))




def aproximate(t,n,U_k):
    range= 2*n+1
    x= linspace(-n,n,range)
    
    for i in range:
        if x[i] >= t:
            try:
                X=[i-2-n,i-1-n,i+1-n,i+2-n]
                break
            except:
                X=[n-3,n-2,n-1,n]
                break
        
    U=[U_k[X[0]] , U_k[X[1]] , U_k[X[2]] , U_k[X[3]]]
    y= polyval(polyfit(X,U,3),t)
    return y
            
            
            
        
    
    
    
    
    

