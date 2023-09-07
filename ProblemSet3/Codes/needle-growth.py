import matplotlib.pyplot as plt
import numpy as np
N=1000
L=200
markersize=10
angle=np.pi/6
base=np.arange(0,L)
height=np.zeros(L)
for j in range(0,N):
    rnd=np.random.randint(0,L)
    for i in range(0,rnd+1):
        height_ball_i=height[rnd]+((rnd-i)*np.tan(angle))
        #print(height_ball_i,height[i])
        if height_ball_i<=height[i]:
            height[i]+=1
            break
    #print(rnd,height)
for i in range(0,L):
    plt.plot([base[i],base[i]],[0,height[i]],'b')
av_height=sum(height)/L
std_height=np.var(height)**0.5
print('av: ',av_height,'  std: ',std_height)
plt.show()


