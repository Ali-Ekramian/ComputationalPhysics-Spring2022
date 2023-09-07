import matplotlib.pyplot as plt
import numpy as np

def triangle(n,x,y,L):
    if n>0:
        triangle(n-1,x,y,L/2)
        triangle(n-1,x+L/2, y,L/2)
        triangle(n-1,x+L/4,y +L/2,L/2)
    else:
        Xs=np.array([x,x+L,x+L/2])
        Ys=np.array([y,y,y+L])
        plt.subplot().fill(Xs,Ys,c='b')

triangle(6, 0, 0, 10)

ft=fontdict={'family':'sans-serif'}
plt.title("Sierpinski Triangle",ft)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


