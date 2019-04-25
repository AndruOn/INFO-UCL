# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 3
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 


from matplotlib import pyplot as plt
from numpy import *
from spline import spline

#
# -1- Interpolation d'un cercle :-)     
#

n = 4;
h = 3*pi/(2*(n+1));
T = arange(0,3*pi/2,h)
X = cos(T); Y = sin(T)

fig = plt.figure()
plt.plot(X,Y,'.r',markersize=10)
t = linspace(0,2*pi,100)
plt.plot(cos(t),sin(t),'--r')

t = linspace(0,3*pi/2,100)
plt.plot(spline(t,h,X),spline(t,h,Y),'-b')
plt.axis("equal"); plt.axis("off")
plt.show()
