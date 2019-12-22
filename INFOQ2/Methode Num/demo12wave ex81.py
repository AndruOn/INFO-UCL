
from numpy import *
from scipy.sparse import spdiags


def waveSolve(beta,nx,nt,c,L,Uo):

  dx = L/nx; dt = dx * beta/c

#
# -1- Implémentation subtile avec spdiags :-)
#

  e = array([0,*ones(nx-1),0])
  D = spdiags([e,-2*e,e],[-1,0,1],nx+1,nx+1)
  D = D.T / (dx*dx)
  print(D.toarray())
  
#
# -2- Implémentation que ferait le titulaire si il devait
#     faire ce programme sur une feuille de papier le jour
#     de l'examen sans ordinateur :-)
#
#     c'est donc cela qu'il faut savoir faire en janvier :-)
#
  
  D = zeros((nx+1,nx+1))
  for i in range(1,nx):
    D[i,i] = -2
    D[i,i+1] = 1
    D[i,i-1] = 1
  D = D / (dx*dx)
  print(D)

#
# -3- Le schéma temporel à bien comprendre !
#
#     Uoo = avant-hier
#     Uo = hier
#     U = aujourd'hui
#
#     Et lorsqu'on passe au jour suivent....
#     Uo devient avant-hier
#     U devient hier :-)
#     et on calcule U à partir de Uo et Uoo
#

  Uoo = (2*Uo + ((c*dt)**2)*D @ Uo)/2
  for t in range(nt):
    U = 2*Uo + ((c*dt)**2 * D @ Uo ) - Uoo
    Uoo = Uo
    Uo = U 
  return U  
  
# ================ Main Program =================================
   
nx = 10; nt = 20; c = 1.0; L = 1.0; beta = 1.0;
X = linspace(0,L,nx+1) 
Uo  = (X/L)**2 * (1-X/L)

U = waveSolve(beta,nx,nt,c,L,Uo)

print(' === u(L/2) = %13.6e  after %d time steps '% (U[nx//2],nt) )

