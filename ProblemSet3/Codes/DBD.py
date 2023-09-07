import matplotlib.pyplot as plt
import numpy as np
N=1000
L=200
base=np.arange(0,200)
height=np.zeros(L)
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]==height[rnd-1] or height[rnd]==height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,rnd,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[rnd],height[(rnd+1)%L]])
        min=np.argmin(narr)
        nrnd=arg[min]
        height[nrnd]+=1
height1=height.copy()
height=np.zeros(L)
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]==height[rnd-1] or height[rnd]==height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,rnd,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[rnd],height[(rnd+1)%L]])
        min=np.argmin(narr)
        nrnd=arg[min]
        height[nrnd]+=1
height2=height.copy()
height2+=height1
height=np.zeros(L)
for i in range(1,N+1):
    rnd=np.random.randint(0,L)
    if height[rnd]==height[rnd-1] or height[rnd]==height[(rnd+1)%L]:
        height[rnd]+=1
    else:
        arg=np.array([rnd-1,rnd,(rnd+1)%L])
        narr=np.array([height[rnd-1],height[rnd],height[(rnd+1)%L]])
        min=np.argmin(narr)
        nrnd=arg[min]
        height[nrnd]+=1
height3=height2+height
for i in range(0,L):
    plt.plot([base[i],base[i]],[0,height1[i]],'b')
    plt.plot([base[i],base[i]],[height1[i],height2[i]],'lightblue')
    plt.plot([base[i],base[i]],[height2[i],height3[i]],'b')
av_height1=sum(height1)/L
av_height2=sum(height2)/L
av_height3=sum(height3)/L
var_height1=np.var(height1)
var_height2=np.var(height2)
var_height3=np.var(height3)
print(av_height1,av_height2,av_height3)
print(var_height1,var_height2,var_height3)
plt.show()
