import matplotlib.pyplot as plt
import numpy as np
N=5000
L=200
markersize=2
data=[100,250,500,700,900,1000,2000,3000,4000,5000,6000,7000,9000,10000,15000,20000]#,30000
#      ,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,750000,1000000,2000000,3000000]
#data=[10,25,50,75,100,125,150,175,200,225,250,275,300,350,400,500]
log_w=np.zeros(len(data))
log_t=np.zeros(len(data))
counter=0
#for L in data:
for N in data:
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
        #plt.plot(base[rnd],height[rnd],c='b',marker='s',markersize=markersize)
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
        #plt.plot(base[rnd],height[rnd],c='lightblue',marker='s',markersize=markersize)
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
        #plt.plot(base[rnd],height[rnd],c='b',marker='s',markersize=markersize)
    height3=height2+height
    std_height=np.var(height3)**0.5
    log_w[counter]=np.log10(std_height)
    log_t[counter]=np.log10(N)
    #log_t[counter]=np.log10(L)
    counter+=1

plt.plot(log_t,log_w,'bo')
fit=np.polyfit(log_t,log_w,1)
m,b=fit[0],fit[1]
print("slope: ",m,"y intersept: ",b)
plt.plot([0,log_t[-1]],[b,(m*log_t[-1])+b])
plt.show()
