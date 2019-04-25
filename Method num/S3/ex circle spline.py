
from numpy import *
from scipy.interpolate import CubicSpline as spline
from matplotlib import pyplot as plt

"""
t=linspace(0,2*pi,101)
for i in [0,3,6,9]:
    
    k= arange(i,i+4)
    X= sin(k*pi/6)
    print("k= ",k)
    Y= cos(k*pi/6)
    print("X= ",X,"Y= ",Y)
    T=k*pi/6
    xh=spline(T,X)(t)
    yh=spline(T,Y)(t)
    plt.plot(xh,yh,label='Spline xh')
    
plt.show()
"""
t=linspace(0,2*pi,101)
k= arange(13)
X= sin(k*pi/6)
print("k= ",k)
Y= cos(k*pi/6)
print("X= ",X,"Y= ",Y)
T=k*pi/6
xh=spline(T,X)(t)
yh=spline(T,Y)(t)
plt.plot(xh,yh,label='Spline xh')
plt.show()