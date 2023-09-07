import matplotlib.pyplot as plt
import numpy as np
import random as rnd

t=np.sqrt(3)/2
def f1(x0,y0):
    x0=x0/2
    y0=y0/2
    return x0,y0
def f2(x0,y0):
    x0=x0/2
    y0=y0/2
    x0=x0+0.5
    return x0,y0
def f3(x0,y0):
    x0=x0/2
    y0=y0/2
    x0=x0+0.25
    y0=y0+0.5*t
    return x0,y0

for i in range(1,5001):
    a=rnd.randint(0,10)
    b=rnd.randint(0,10)
    for j in range(1,20):
        u=rnd.randint(1,3)
        if u==1:
            a,b=f1(a,b)
        if u==2:
            a,b=f2(a,b)
        if u==3:
            a,b=f3(a,b)
    plt.plot(a,b,'bo',markersize=0.75)
    
plt.show()
