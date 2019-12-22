import matplotlib.pyplot as Plt
import time
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve
from numpy import * 

tic= time.time()
factor= 10
nx=  7*factor ; ny= 4*factor
n= nx * ny 
h= 2/(nx-1)
"A =eye(n)"
A= sparse.dok_matrix(sparse.eye(n),dtype='float32')
B= zeros(n)

for i in range(1,nx-1):
    for j in range(1,ny-1):
        index= i + j*nx
        A[index,index]= 4
        A[index,index-1]= -1
        A[index,index+1]= -1
        A[index,index-nx]= -1
        A[index,index+nx]= -1
        B[index]=1

A=  A/(h*h)
"U= solve(A,B)"
U= spsolve(A.tocsr(),B)
toc = time.time() - tic
print("Elapsed time is %f seconds" %  toc)

X= linspace(-2,2,nx)
Y= linspace(-1,1,ny)
Plt.figure("Maillage")
Plt.hlines(Y,X.min(),X.max(),color="black",linewidths=0.1)
Plt.hlines(X,Y.min(),Y.max(),color="black",linewidths=0.1)


Plt.figure("Un joli graphique")
U= U.reshape(ny,nx)
Plt.axis("equal"); Plt.axis("off")
Plt.contour(X,Y,U,10,cmap='matplotlib.cm.jet')
Plt.contour(X,Y,U,10,colors='k',linewidths=1)
Plt.show()

