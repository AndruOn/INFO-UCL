from scipy.linalg import solve


def n_r(l):
    x,y = l
    fx=( -(x**2 - y) , -(4*x**2 + 9*y**2 - 8*x - 32) )
    
    derivfx=( [2*x , -1] , [8*x -8 , 18*y] )
    
    deltax,deltay = solve(derivfx,fx)
    newx=x+deltax
    newy=y+deltay
    return newx,newy

n=0
x,y= (1.4,2.0)
tol=1
while tol > 0.0001 and n < 10000:
    newx,newy = n_r((x,y))
    tol= max(newx-x,newy-y)
    x,y = newx,newy
    n+=1
    
print(x,y)