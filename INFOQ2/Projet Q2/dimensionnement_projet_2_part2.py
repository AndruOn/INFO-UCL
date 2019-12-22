from numpy import *

inp = input("k,C2,R1= ")
inp= inp.split(",")

k=float(inp[0])
C2=float(inp[1])
R1=float(inp[2])
print(k,C2,R1)

Rz=9500
L2=27e-6
omegacarré=((Rz**2)*C2-L2)/((Rz**2)*(C2**2)*L2)
omega= sqrt(omegacarré)

L1=R1 / (Rz*C2*(k**2)*omegacarré)

C1=1/ (L1*omegacarré)

f=omega/(2*pi)

n= L1 * 5e-4 / (4* (pi**2) * 1e-7 * 0.0045**2)

print("\n")
print("imposés")
print("k=",k)
print("R1=",R1)
print("Rz=",Rz)
print("L2=",L2)
print("C2=",C2)
print("\n")
print("obtenues")
print("L1=",L1)
print("C1=",C1)
print("omega=",omega)
print("f=",f)

print("n=",n)
                   
