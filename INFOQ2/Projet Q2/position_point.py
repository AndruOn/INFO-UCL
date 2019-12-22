import numpy as np
from scipy.linalg import norm,solve

def pospoint(l):
    n= len(l)
    maxun= 0
    maxdeux= 0
    pos=[0,0]
    for i in range(n):
        if l[i] >= maxun:
            maxdeux= maxun
            maxun= l[i]
    maxi= l.index(maxun)
    maxdeuxi= l.index(maxdeux)
    print("maxun= ",maxun," index= ",maxi)
    print("maxdeux= ",maxdeux," index= ",maxdeuxi)
    
    if maxi >= maxdeuxi:
        if abs(maxdeuxi-maxi)== 1:     ##horiontal
            disthoriz= maxdeux / maxun
            pos[0]= maxi % 3 + disthoriz
            print("posx= ",pos[0])
            a= maxi + 3
            b= maxi - 3
            if a <= 9 and 0 <= b :
                if l[a] >= l[b]:              ##vertical
                    distvertic= l[b] / l[a]
                    pos[1]= a // 3 - distvertic
                    print("posy= ",pos[1])
                else:
                    distvertic= l[a] / l[b]
                    pos[1]= a // 3 + distvertic
                    print("posy= ",pos[1])
            else:
                if a <= 9:
                    distvertic= a / maxun
                    pos[1]= maxun  
                    
                
                
            return pos                            
        
        elif abs(maxdeuxi-maxi)== 3:    ##vertical
            distvertic= maxdeux / maxun
            pos[1]= maxi // 3 - distvertic
            
            
    else:
        if abs(maxdeuxi-maxi)== 1:     ##horiontal
            disthoriz= maxdeux / maxun 
            pos[0]= maxi % 3 - disthoriz
         
        elif abs(maxdeuxi-maxi)== 3:   #vertical
            distvertic= maxdeux / maxun
            pos[1]= maxi // 3 + distvertic
    

    
def pos_tri(l):
    dic={
    0:{"droite":1,"bas":3},
    1:{"gauche":0,"droite":2,"bas":4},
    2:{"gauche":1,"bas":5},
    3:{"haut":0,"droite":4,"bas":6},
    4:{"gauche":3,"haut":1,"droite":5,"bas":7},
    5:{"gauche":4,"haut":2,"bas":8},
    6:{"haut":3,"droite":7},
    7:{"gauche":6,"haut":4,"droite":8},
    8:{"gauche":7,"haut":5},
        } 
    n= len(l)
    maxa= max(l)
    maxi= l.index(maxa)
    print("maxun= ",maxa," index= ",maxi)
    dico= dic[maxi]
    index_voisins=list(dico.values())
    print("index_voisins= ",index_voisins)
    if len(index_voisins)==2:
        print("max dans un coin")
        return "formule"
    voisins=[]
    for i in index_voisins:
        voisins.append(l[i])
    print("voisins= ",voisins)
     
   
    
def pos_paquets(l):
    paquets=[[0,1,3,4],[1,2,4,5],[3,4,6,7],[4,5,7,8]]
    sums=[0,0,0,0]
    formule= 24+18

    for i in range(4):
        somme=0
        for j in range(4):
            somme+= l[paquets[i][j]]
        print("somme paquet%s= " % (i),somme)
        sums[i]= somme
    paquet= paquets[ sums.index(max(sums)) ]
    print("paquetmax= ",paquet)
    
    if  l[paquet[0]] + l[paquet[1]] > l[paquet[2]] + l[paquet[3]] :
        x= paquet[0] %3 + formule
    
    else:
        x= paquet[2] %3 + formule
        
    if l[paquet[0]] + l[paquet[2]] > l[paquet[1]] + l[paquet[3]] :
        y= paquet[0] //3 + formule
        
    else:
        y= paquet[1] //3 + formule
    
    return x,y
    




def bis_One_NewtRaph(X,données):
    x0,y0,d0 , x1,y1,d1 , x2,y2,d2 = données
    x,y,alpha = X
    
    fx=( -((x-x0)**2 + (y-y0)**2 -(d0**2)/alpha) , -((x-x1)**2 + (y-y1)**2 -(d1**2)/alpha) , -((x-x2)**2 + (y-y2)**2 -(d2**2)/alpha) )
    
    df0dx= (x-x0)*2*x
    df0dy= (y-y0)*2*y
    df0dalpha= (d0**2)/(alpha**2)
    df1dx= (x-x1)*2*x
    df1dy= (y-y1)*2*y
    df1dalpha= (d1**2)/(alpha**2)
    df2dx= (x-x2)*2*x
    df2dy= (y-y2)*2*y
    df2dalpha= (d2**2)/(alpha**2)
    
    derivfx=np.array(( (df0dx,df0dy,df0dalpha),(df1dx,df1dy,df1dalpha),(df2dx,df2dy,df2dalpha) ))
    
    delta = solve(derivfx,fx)

    newx=(x,y,alpha) + delta

    return newx

    
# =========================================================================
  
def bis_iter_NewtRaph(l,paquet,nmax,ancienX):
    x = ancienX
    n = 0
    tol = 10e-12; delta = tol+1
    paquetvalues= [ l[paquet[0]],l[paquet[1]],l[paquet[2]],l[paquet[3]] ]
    indexmin= paquetvalues.index(min(paquetvalues))
    
    print("paquet= ",paquet,"paquetvalues= ",paquetvalues)
    del paquet[indexmin] 
    del paquetvalues[indexmin]
    print("paquet= ",paquet,"   paquetvalues= ",paquetvalues)
    
    données= ( paquet[0]%3,paquet[0]//3,paquetvalues[0] , paquet[1]%3,paquet[1]//3,paquetvalues[1] , paquet[2]%3,paquet[2]//3,paquetvalues[2])
    print("données (x0,y0,d0 , x1,y1,d1 , x2,y2,d2)= ",données)
    
    while (norm(delta) > tol and n < nmax):
        xold = x
        print("x,y= ",xold[0],xold[1])
        x = One_NewtRaph(xold,données)
        delta = x-xold
        n = n+1
        
    return x[0],x[1]
  
# =========================================================================

   
def bis_pos_NewtRaph(l,ancienX):
    paquets=[[0,1,3,4],[1,2,4,5],[3,4,6,7],[4,5,7,8]]
    sums=[0,0,0,0]

    for i in range(4):
        somme=0
        for j in range(4):
            somme+= l[paquets[i][j]]
        print("somme paquet%s= " % (i),somme)
        sums[i]= somme
    paquet= paquets[ sums.index(max(sums)) ]
    print("paquetmax= ",paquet)
    
    return iter_NewtRaph(l,paquet,10,ancienX)

# =========================================================================

def One_NewtRaph(X,paquetvalues,paquetindex):
    d0,d1,d2,d3 = paquetvalues
    index0,index1,index2 = paquetindex
    h,c,alpha = X
    
    
    fx= ( - h**2 - c**2 + (d0**2)/alpha , - (1-h)**2 - c**2 + (d1**2)/alpha , - h**2 - (1-c)**2 + (d2**2)/alpha , - (1-h)**2 - (1-c)**2 + (d3**2)/alpha )
    fx= ( fx[index0],fx[index1],fx[index2] )
    
    df0= (2*h,2*c,(2*d0**2)/(alpha**2))
    df1= (2*h-2,2*c,(2*d1**2)/(alpha**2))
    df2= (2*h,2*c-2,(2*d2**2)/(alpha**2))
    df3= (2*h-2,2*c-2,(2*d3**2)/(alpha**2))
    
    df= [df0,df1,df2,df3]
    df= ( df[index0],df[index1],df[index2] )
    
    delta = solve(df,fx)
    
    newx= X + delta

    return newx

    
# =========================================================================
  
def iter_NewtRaph(l,paquet,nmax,tol,ancienX):
    x = ancienX
    n = 0
    tol = 10e-7; delta = tol+1
    paquetvalues= [ l[paquet[0]],l[paquet[1]],l[paquet[2]],l[paquet[3]] ]
    indexmin= paquetvalues.index(min(paquetvalues))
    paquetindex= [0,1,2,3]
    
    print("paquet= ",paquet,"paquetvalues= ",paquetvalues)
    del paquetindex[indexmin]
    del paquet[indexmin] 
    print("paquet= ",paquet,"   paquetvalues= ",paquetvalues,"    paquetindex= ",paquetindex)
    
    
    while (norm(delta) > tol and n < nmax):
        xold = x
        print("x,y,alpha= ",xold[0],xold[1],xold[2])
        x = One_NewtRaph(xold,paquetvalues,paquetindex)
        delta = x-xold
        n = n+1
        
    return x[0],x[1]
  
# =========================================================================

   
def pos_NewtRaph(l,ancienX,nmax,tol):
    paquets=[[0,1,3,4],[1,2,4,5],[3,4,6,7],[4,5,7,8]]
    sums=[0,0,0,0]
    
    for i in range(4):
        somme=0
        for j in range(4):
            somme+= l[paquets[i][j]]
        print("somme paquet%s= " % (i),somme)
        sums[i]= somme
    paquet= paquets[ sums.index(max(sums)) ]
    dist=map_vtod(l)
    print("distances= ",dist)
    print("paquetmax= ",paquet)
    
    return iter_NewtRaph(dist,paquet,nmax,tol,ancienX)
   
   
   
def map_vtod(l):
    n=len(l)
    newl= np.zeros(n)
    for i in range(n):
        newl[i]= 1/((5000 - l[i])**(1/2))
    return newl
        
   
   
#print(map_vtod([0,100,200,300,400,500,2000,4999,5000]))
   
   
   
   

   
   
   
   
   
  
   
   
   
    
if __name__ == '__main__':
    
    l1= [2,2,4,15,20,1,3,4,2]
    l2= [12,13,47,3,2,10,0,1,0]
    l3= [2,0,0,7,30,28,1,19,12]
    l= [l1,l2,l3]
    for lis in range(len(l)):
        for i in range(9):
            l[lis][i]= l[lis][i] * 100 

    for liste in l:
        print("--------------------------------------------------------------------------------------------------------------------------")
        print("liste= %s" % (liste))
        for i in range(3):
            print(" %s   %s   %s" % (liste[i*3],liste[(i*3)+1],liste[(i*3)+2]) )
        """
        print("---------------technique 1 (posxy)---------------")
        print("position: ",pospoint(liste))
        print("---------------technique 2 (tri)---------------")
        print("position: ",pos_tri(liste))
        print("---------------technique 3 (paquets)---------------")
        print("position: ",pos_paquets(liste))
        """
        print("---------------technique 4 (paquets - NewtonRaphson)---------------")
        print("position: ",pos_NewtRaph(liste,(0.5,0.5,4500),nmax=20,tol=10e-10))
        print("-------------------------------------------------------------------------------------------------------------------------")
        print() 



    print()
    print(" 0  1  2")
    print(" 3  4  5")
    print(" 6  7  8")
