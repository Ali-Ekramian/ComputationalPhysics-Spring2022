import matplotlib.pyplot as plt
import numpy as np
N=20000
L=200
markersize=1
base=np.arange(1,L+1)
height=np.zeros(L)
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]>=height[rnd-1] and height[rnd]>=height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[(rnd+1)%L]])
        max=np.argmax(narr)
        nrnd=arg[max]
        height[rnd]=height[nrnd]
    plt.plot(base[rnd],height[rnd],c='b',marker='s',markersize=markersize)
height1=height.copy()
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]>=height[rnd-1] and height[rnd]>=height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[(rnd+1)%L]])
        max=np.argmax(narr)
        nrnd=arg[max]
        height[rnd]=height[nrnd]
    plt.plot(base[rnd],height[rnd],c='lightblue',marker='s',markersize=markersize)
height2=height.copy()
height2+=height1
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]>=height[rnd-1] and height[rnd]>=height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[(rnd+1)%L]])
        max=np.argmax(narr)
        nrnd=arg[max]
        height[rnd]=height[nrnd]
    plt.plot(base[rnd],height[rnd],c='b',marker='s',markersize=markersize)
height3=height2+height
av_height1=sum(height1)/L
av_height2=sum(height2)/L
av_height3=sum(height3)/L
std_height1=np.var(height1)**0.5
std_height2=np.var(height2)**0.5
std_height3=np.var(height3)**0.5
print(av_height1,av_height2,av_height3)
print(std_height1,std_height2,std_height3)
print(height1,height2,height3)
plt.show()
