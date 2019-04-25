from numpy import *
from matplotlib import pyplot as plt




t=linspace(-3,3,1000)
X,Y=meshgrid(t,t)
Z=X+Y*1j
valeur_de_stabilité= abs( 1+Z+(3/4)*(Z**2) + sqrt( (1+Z+(3/4)*(Z**2))**2 - Z**2 )) /2
plt.contourf(X,Y,valeur_de_stabilité,arange(0,1.1,0.1),cmap=plt.cm.jet_r)
plt.show()