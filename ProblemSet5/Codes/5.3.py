import numpy as np
import matplotlib.pyplot as plt
import random
def step(pr):
    rnd=np.random.rand()
    if rnd<=pr:
        return 1
    else:
        return -1
color=['gray','pink','orange','g','r','b','purple','brown','y','c','k']
for p in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
    life=[]
    X=[]
    for x in range(21):
        x=x-10
        I=[]
        X.append(x)
        for j in range(1000):
            i=0
            y=x
            while True:
                y+=step(p)
                if y<-10 or y>10:
                    break
                i+=1
            I.append(i)
        I_av=sum(I)/len(I)
        life.append(I_av)
    plt.plot(X,life,'o--',color=color[int(p*10)],label=' p = '+str(p),markersize=2.5)
plt.grid(True)
plt.legend()
plt.show()    