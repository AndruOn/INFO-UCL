from scipy.sparse import dok_matrix
from scipy.sparse.linalg import spsolve



def poissonSolve (nx,ny):
    n= nx*ny; h= 2/(ny-1)
    A= dok_matrix((n,n),dtype=float32); B= zeros(n)
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            index= i + j*nx
            A[index,index]= 4.0
            A[index,index+1]= -1.0
            A[index,index-1]= -1.0
            A[index,index-nx]= -1.0
            A[index,index+nx]= -1.0
            B[index]= 1
    return solve(A,B).reshape(ny,nx)
            

