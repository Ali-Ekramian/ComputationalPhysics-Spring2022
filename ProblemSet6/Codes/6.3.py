import numpy as np
import matplotlib.pyplot as plt
import random
J=1000
N=np.array([5,10,100,1000])
for n in N:
    counts=np.array([])
    for j in range(J):
        data=np.array([])
        for i in range(n):
            rnd=random.randint(0,9)
            data=np.append(data,rnd)
        #print("data : ",data)
        sum_data=np.sum(data)
        counts=np.append(counts,sum_data)
    #print("Counts : ",counts)
    bin=(-0.00004871*n*n)+(0.0591463*n)+9.56376
    bin,edges,z=plt.hist(counts,bins=int(bin)+1)
    std=np.std(counts)
    mean=np.average(counts)
    x=np.linspace(min(counts),max(counts),100)
    y=np.exp(-0.5*((x-mean)/std)**2)*max(bin)
    plt.plot(x,y,'r')
    plt.xlabel("sum of array")
    plt.ylabel("# of Repated")
    plt.title(f"Histogram of sum N={n} with {J} repeats")
    plt.show()