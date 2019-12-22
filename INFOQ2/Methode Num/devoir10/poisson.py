# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 10
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# VOUS POUVEZ IMPORTER TOUS LES PACKAGES PRESENTS SUR LE SERVEUR

from numpy import *
from numpy.linalg import solve

#
# A MODIFIER
#     - pour modifier le demaine de calcul en retirant
#       le coin supérieur droit
#     - pour tirer profit du caractère creux de la matrice
#
#

def poissonSolve(nCut):
    n = 2*nCut + 1; m = n*n; h = 2/(n-1) 

    A = eye(m); B = zeros(m)  
    for i in range(nCut,n-1):
        for j in range(nCut,n-1):
            index = i + j*n
            A[index,index] = 4
            A[index,index-1] = -1
            A[index,index+1] = -1
            A[index,index+n] = -1
            A[index,index-n] = -1
            B[index] = 1

    for i in range(1,n-1):
        for j in range(1,nCut):
            index = i + j*n
            A[index,index] = 4
            A[index,index-1] = -1
            A[index,index+1] = -1
            A[index,index+n] = -1
            A[index,index-n] = -1
            B[index] = 1
      
    return solve(A/(h*h),B).reshape(n,n)


