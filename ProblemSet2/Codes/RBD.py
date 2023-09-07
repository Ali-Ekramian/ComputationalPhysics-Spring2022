import matplotlib.pyplot as plt
import numpy as np
N=1000000
base=np.arange(1,201)
height=np.zeros(200)
for i in range(1,N+1):
    rnd=np.random.randint(1, 201)
    height[(rnd-1)]+=1
height1=height.copy()
height=np.zeros(200)
for i in range(1,N+1):
    rnd=np.random.randint(1, 201)
    height[(rnd-1)]+=1
height2=height.copy()
height2+=height1
height=np.zeros(200)
for i in range(1,N+1):
    rnd=np.random.randint(1, 201)
    height[(rnd-1)]+=1
height3=height2+height
for i in range(0,200):
    plt.plot([base[i],base[i]],[0,height1[i]],'b')
    plt.plot([base[i],base[i]],[height1[i],height2[i]],'lightblue')
    plt.plot([base[i],base[i]],[height2[i],height3[i]],'b')
av_height1=sum(height1)/200
av_height2=sum(height2)/200
av_height3=sum(height3)/200
print(av_height1,av_height2,av_height3)
plt.show()
