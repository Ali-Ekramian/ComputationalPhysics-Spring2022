import numpy as np
import matplotlib.pyplot as plt
import random
N=1000
b=2
a=0
#Simple Sampling
F=np.array([])
RND=np.array([])
for i in range(N):
    rnd=random.uniform(a,b)
    fr=np.exp(-(rnd**2))
    F=np.append(F,fr)
    RND=np.append(RND,rnd)
#print(F)
avg=np.average(F)
std=np.std(F)
S=avg*(b-a)
print(f"The Answer of Integral is: {S}")
xs=np.linspace(a,b,100)
ys=np.exp(-(xs**2))
avgs=np.array(([avg]*100))
plt.plot(xs,ys,'r',label=r'The $e^{-x^2}$')
plt.plot(RND,F,'bo',label=r'Random points and their f(random)')
plt.plot(xs,avgs,'g',markersize=1,label=r'Average of f')
plt.plot(0,0,'w',markersize=0,label=r'Answer of $\int_0^2 e^{-x^2}dx$ is '+str(round(S,3)))
plt.title(r'Integral of $\int_0^2 e^{-x^2}dx$ with Simple Sampling')
plt.legend()
plt.show()

#Important Sampling
F=np.array([])
G=np.array([])
RND=np.array([])
for i in range(N):
    rnd=-np.log(1-(random.uniform(0,1-(np.exp(-2)))))
    fr=np.exp(-(rnd**2))
    F=np.append(F,fr)
    G=np.append(G,np.exp(-rnd))
    RND=np.append(RND,rnd)
#print(F)
ARG=np.array([])
for i in range(N):
    arg=(F[i]/G[i])*np.exp(-RND[i])
    ARG=np.append(ARG,arg)
avg=0.864*np.average(ARG)
#avg=0.86*np.average(np.divide(F,G))
S=avg*(b-a)
print(f"The Answer of Integral is: {S}")
xs=np.linspace(a,b,100)
ys=np.exp(-(xs**2))
avgs=np.array(([avg]*100))
plt.plot(xs,ys,'r',label=r'The $e^{-x^2}$')
plt.plot(RND,F,'bo',label=r'Random points and their f(random)')
plt.plot(xs,avgs,'g',markersize=1,label=r'Average of f')
plt.plot(0,0,'w',markersize=0,label=r'Answer of $\int_0^2 e^{-x^2}dx$ is '+str(round(S,3)))
plt.title(r'Integral of $\int_0^2 e^{-x^2}dx$ with Important Sampling')
plt.legend()
plt.show()    

