import numpy as np
import matplotlib.pyplot as plt
import random
N=10000
sigma=1
X=np.array([])
Y=np.array([])
for i in range(N):
    rho=random.random()
    theta=random.uniform(0,2*np.pi)
    x=np.sqrt(-2*sigma*sigma*np.log(1-rho))*np.cos(theta)
    y=np.sqrt(-2*sigma*sigma*np.log(1-rho))*np.sin(theta)
    X=np.append(X,x)
    Y=np.append(Y,y)
bin,edges,z=plt.hist(X,bins=30)
std=np.std(X)
mean=np.average(X)
x=np.linspace(min(X),max(X),100)
y=np.exp(-0.5*((x-mean)/std)**2)*max(bin)
plt.plot(x,y,'r')
plt.xlabel("Random Gaussian Generated Numbers")
plt.ylabel("# of Repated")
plt.title(f"Histogram of {N} Random Gaussian Generated Numbers")
plt.show()
plt.scatter(X,Y,s=3,marker='o')
plt.title(f"Plot of ({N},{N}) Random Gaussian Generated Numbers in X,Y Plane")
plt.show()