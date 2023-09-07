import matplotlib.pyplot as plt
import numpy as np
import random as rnd

t=np.sqrt(3)/2
rad=np.pi/180
def f1(x0,y0):
    x0*=0.9
    y0*=0.9
    R5=np.array([[np.cos(-5*rad), -np.sin(-5*rad)], [np.sin(-5*rad), np.cos(-5*rad)]])
    res=R5 @ (np.array([x0,y0]))
    x0,y0=res[0],res[1]
    x0+=0.1
    y0+=0.4
    return x0,y0
def f2(x0,y0):
    x0*=0.3
    y0*=0.3
    R5=np.array([[np.cos(40*rad), -np.sin(40*rad)], [np.sin(40*rad), np.cos(40*rad)]])
    res=R5 @ (np.array([x0,y0]))
    x0,y0=res[0],res[1]
    x0+=0.5
    y0+=0.4
    return x0,y0
def f3(x0,y0):
    x0*=(-0.35)
    y0*=0.35
    R5=np.array([[np.cos(-60*rad), -np.sin(-60*rad)], [np.sin(-60*rad), np.cos(-60*rad)]])
    res=R5 @ (np.array([x0,y0]))
    x0,y0=res[0],res[1]
    x0+=0.6
    y0+=-0.1
    return x0,y0
def f4(x0,y0):
    x0*=0.01
    y0*=0.2
    R5=np.array([[np.cos(-3*rad), -np.sin(-3*rad)], [np.sin(-3*rad), np.cos(-3*rad)]])
    res=R5 @ (np.array([x0,y0]))
    x0,y0=res[0],res[1]
    x0+=0.5
    y0+=-0.3
    return x0,y0
for i in range(1,20001):
    a=rnd.randint(0,10)
    b=rnd.randint(0,10)
    for j in range(1,20):
        u=rnd.randint(1,7)
        if u==3:
            a,b=f4(a,b)
        if u==1:
            a,b=f2(a,b)
        elif u==2:
            a,b=f3(a,b)
        else:
            a,b=f1(a,b)
    plt.plot(a,b,'go',markersize=0.65)

plt.show()
