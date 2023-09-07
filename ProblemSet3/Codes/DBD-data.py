import matplotlib.pyplot as plt
import numpy as np
N=50000
L=200
#data=[100,250,500,750,1000,2500,5000,7500,10000,20000,30000,40000,50000,60000,
#      70000,80000,90000,100000,200000,300000,400000,500000,750000,1000000,2000000,3000000]
data=[10,25,50,75,100,125,150,175,200,225,250,275,300,350,400,500]
log_w=np.zeros(len(data))
log_t=np.zeros(len(data))
counter=0
#for N in data:
for L in data:
    base=np.arange(1,L+1)
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
    std_height=np.var(height3)**0.5
    log_w[counter]=np.log10(std_height)
    #log_t[counter]=np.log10(N)
    log_t[counter]=np.log10(L)
    counter+=1

plt.plot(log_t,log_w,'bo')
fit=np.polyfit(log_t,log_w,1)
m,b=fit[0],fit[1]
print("slope: ",m,"y intersept: ",b)
plt.plot([0,log_t[-1]],[b,(m*log_t[-1])+b])
plt.show()