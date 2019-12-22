# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 8
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#

from scipy.linalg import norm,solve

#
# TOUTE AUTRE INSTRUCTION CONTENANT import / from SERA AUTOMATIQUEMENT SUPPRIMEE
#
# =========================================================================

def laddersIterate(geometry,x):
    a,b,c = geometry
    x,y = x
    
    fx=( -((x+y)*(x**2+c**2)**(1/2)-b*x) , -((x+y)*(y**2+c**2)**(1/2)-a*y) )
    
    rac= (x**2+c**2)**(1/2)
    df1dx= rac + ((x+y)*x/rac) - b
    df1dy= rac
    rac= (y**2+c**2)**(1/2)
    df2dx= rac
    df2dy= rac + ((x+y)*y/rac) - a
    
    derivfx=( (df1dx,df1dy),(df2dx,df2dy) )   
    
    delta = solve(derivfx,fx)

    newx=(x,y) + delta

    return newx

    
# =========================================================================
  
def laddersSolve(geometry,tol,nmax):
    x = (1.0,1.5); tol = 10e-12; nmax = 50
    n = 0; delta = tol+1
    while (norm(delta) > tol and n < nmax):
        xold = x
        x = laddersIterate(geometry,xold)
        delta = x-xold; n = n+1
    return x
  
# =========================================================================
