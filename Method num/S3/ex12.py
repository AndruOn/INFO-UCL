import numpy as np
from scipy.interpolate import CubicSpline as spline
from matplotlib import pyplot as plt


T=[2,3,4,5]
def t_h(T,x,y):
    X=[-1,-1,1,1]
    Y=[-1,1,1,-1]
    txh= spline(X,T)(x)
    tyh= spline(Y,T)(x)
    
    return (txh,tyh)

