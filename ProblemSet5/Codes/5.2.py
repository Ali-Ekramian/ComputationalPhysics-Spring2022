import numpy as np
import matplotlib.pyplot as plt
p=0.5
q=1-p
Num=100
def step(pr):
    rnd=np.random.rand()
    if rnd<=pr:
        return 1
    else:
        return -1
AVG=[]
STD=[]
VAR=[]
T=[]
N=[]
t=0
n=0
while n<=Num:
    final=[]
    for j in range(100):
        x=0
        for i in range(n):
            x+=step(p)
            #print(x)
        final.append(x)
    av=sum(final)/len(final)
    var=np.var(final)
    std=(var)**0.5
    AVG.append(av)
    VAR.append(var)
    STD.append(std)
    T.append(t)
    N.append(n)
    t+=1
    n+=10
    #print(final)
    #print("\n","AVG = ",av,"STD = ",std)

plt.plot(N,AVG,'bo')
plt.plot(N,VAR,'ro')
fit=np.polyfit(N,VAR,1)
m,b=fit[0],fit[1]
print("slope for σ^2 : "  ,m,"// y intersept for σ^2 : ",b)
plt.plot([0,N[-1]],[b,(m*N[-1])+b],color='red',label=r'$\sigma^2 $')
fit_av=np.polyfit(T,AVG,1)
m_av,b_av=fit_av[0],fit_av[1]
print("slope for <x(t)> : "  ,m_av,"// y intersept for <x(t)> : ",b_av)
plt.plot([0,N[-1]],[b_av,(m_av*N[-1])+b_av],color='blue',label=r'$ \langle x(t)\rangle  $')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel(r'$\langle x(t)\rangle \quad & \quad \sigma^2$')
plt.legend()
plt.show()
