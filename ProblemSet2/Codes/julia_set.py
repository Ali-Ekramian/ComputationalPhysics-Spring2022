import matplotlib.pyplot as plt
import numpy as np
import random as rnd
def f(z,c):
    fz=z**2+c
    return fz
c=complex(-0.2,0.3)
print(c)
for j in range(1,100001):
    x,y=rnd.random(),rnd.random()
    z=complex(x,y)
    for i in range(1,5):
        z=f(z,c)
        #print(z)
    norm=(z.real**2+z.imag**2)**0.5
    if norm>1:
        plt.plot(z.real,z.imag,'bo',markersize=0.5)
    if norm<=1:
        plt.plot(z.real,z.imag,'ro',markersize=0.5)

plt.xlim([-2,2])
plt.ylim([-2,2])
plt.show()
