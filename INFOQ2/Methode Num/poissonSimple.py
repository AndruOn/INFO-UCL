
#
# A very simple (not the most efficient !) implementation 
# to solve the Poisson's equation
#
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *
from numpy.linalg import solve
from scipy.sparse import dok_matrix
from scipy.sparse.linalg import spsolve 

import matplotlib 
import matplotlib.pyplot as plt 
matplotlib.rcParams['toolbar'] = 'None'
myColorMap = matplotlib.cm.jet

from timeit import default_timer as timer

# =========================================================================

def poissonSolve(nx,ny):  
  n = nx*ny; h = 2/(ny-1)
  A = eye(n); B = zeros(n)   
  for i in range(1,nx-1):
    for j in range(1,ny-1):
      index = i + j*nx
      A[index,index]    =  4.0
      A[index,index-1]  = -1.0
      A[index,index+1]  = -1.0
      A[index,index-nx] = -1.0
      A[index,index+nx] = -1.0
      B[index] = 1  
  return solve(A,B).reshape(ny,nx) 

# =========================================================================

  
def poissonSolveSparse(nx,ny):
  n = nx*ny; h = 2/(ny-1)
  A = dok_matrix((n,n),dtype=float32)
  B = zeros(n)
  for i in range(n):
    A[i,i] = 1.0  
  for i in range(1,nx-1):
    for j in range(1,ny-1):
      index = i + j*nx
      A[index,index]    =  4.0
      A[index,index-1]  = -1.0
      A[index,index+1]  = -1.0
      A[index,index-nx] = -1.0
      A[index,index+nx] = -1.0
      B[index] = 1
  A = A / (h*h)
  return spsolve(A.tocsr(),B).reshape(ny,nx)  
  
# ============================= mainProgram ===============================

nx = ny = 100;
print(' === Considering nx=ny=%d' % nx)
tic = timer()
U = poissonSolve(nx,ny)
toc = timer() - tic
print(' === Full solver   : elapsed time is %f seconds.' % toc)
tic = timer()
U = poissonSolveSparse(nx,ny)
toc = timer() - tic
print(' === Sparse solver : elapsed time is %f seconds.' % toc)


plt.figure("Temperature")
Xg,Yg = meshgrid(linspace(-1,1,nx),linspace(-1,1,ny))
plt.contourf(Xg,Yg,U,10,cmap=myColorMap)
plt.contour(Xg,Yg,U,10,colors='k',linewidths=1)
plt.axis("equal"); plt.axis("off")
plt.show()

# =========================================================================

