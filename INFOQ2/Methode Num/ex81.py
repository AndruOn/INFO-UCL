import numpy as np


def wavesolve(beta,nx,nt,L,Uo):
    U_0= Uo
    U_bis= U_0
    U_1= np.zeros(nx)
    for i in range(1,nx-1):
        U_1[i]= U_bis[i] + beta**2*(U_bis[i+1]-2*U_bis[i]+U_bis[i-1])/2
        
    for t in range(nt):
        U_bis= U_1.copy()
        for i in range(1,nx-1):
            U_1[i]= 2*U_bis[i] + beta**2*(U_bis[i+1]-2*U_bis[i]+U_bis[i-1]) - U_0[i]
        U_0= U_bis.copy()
    return U_1


beta=1.0; nx=10 ; nt= 20; L=1.0;c=1.0
X= np.linspace(0,L,nx+1)
Uo= (X/L)**2 * (1-X/L)

U= wavesolve(beta,nx,nt,L,Uo)
print(U)

