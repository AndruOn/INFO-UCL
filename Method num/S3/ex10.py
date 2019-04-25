
import numpy as np
from scipy.interpolate import CubicSpline as spline
from matplotlib import pyplot as plt


x=np.linspace(1970,1996,101)
X=[1975,1980,1985,1990]
U=[70.2,70.2,70.3,71.2]
us= spline(X,U)
up= np.polyval(np.polyfit(X,U,3), x)



plt.plot(x,us(x),label='Spline ')
plt.plot(x,up,label='poly ')

plt.show()

print("us(1970)= ",us(1970))
print("us(1995)= ",us(1995))
print("up(1970)= ",np.polyval(np.polyfit(X,U,3), 1970))
print("up(1995)= ",np.polyval(np.polyfit(X,U,3), 1995))


plt.plot(x,us(x)-up,label='erreur ')
plt.show()