import matplotlib.pyplot as plt
import numpy as np
angle=np.pi/4
R=np.array([[np.cos(angle),-np.sin(angle)],
            [np.sin(angle),np.cos(angle)]])
R=R/np.sqrt(2)
def Dragon(n):
    if n<1:
        return [[0,0],[1,0]]
    else:
        pts0=Dragon(n-1)
        pts=[]
        for x,y in pts0:
            [x1,y1]=R @ [x,y]
            pts.append([x1,y1])
        for x,y in reversed(pts0):
            [x2,y2]=[1,0] - R.T @ [x,y]
            pts.append([x2,y2])
        return pts
points = Dragon(15)
x = [p[0] for p in points]
y = [p[1] for p in points]
print(x)
print(y)
plt.plot(x,y)
ft=fontdict={'family':'sans-serif'}
plt.title("Heighway Dragon",ft)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

