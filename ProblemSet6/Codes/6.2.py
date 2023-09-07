import numpy as np
import matplotlib.pyplot as plt
import random

N=100000
T=np.array([])
N_STD=np.array([])
n=50
while n<=N:
    numbers=np.array([])
    num_after_4=np.array([])
    for i in range(n):
        rnd=random.randint(0,9)
        numbers=np.append(numbers,rnd)
    counts=np.zeros(10)
    for i in range(n):
        if numbers[i]==4:
            num_after_4=np.append(num_after_4,numbers[(i+1)%(len(numbers))])
        else:
            continue
    for i in num_after_4:
        counts[int(i)]+=1
    std=(np.var(counts))**0.5
    n_std=std/len(num_after_4)
    T=np.append(T,len(num_after_4))
    N_STD=np.append(N_STD,n_std)
    n+=n
print("  norm std : ",N_STD)
print("  T : ",T)
log_STD=np.log(N_STD)
log_T=np.log(T)
plt.plot(log_T,log_STD,'bo')
fit=np.polyfit(log_T,log_STD,1)
m,b=fit[0],fit[1]
print("slope for log STD(T) : "  ,m,"// y intersept for log STD(T) : ",b)
plt.plot([0,log_T[-1]],[b,(m*log_T[-1])+b],color='blue',label=r'fited line $\frac{\sigma (N)}{N}$ in logaritmic scale')
plt.grid(True)
plt.xlabel("log of Time")
plt.ylabel("log of normilized STD")
plt.title("log of normilized STD with respect to time (number)")
plt.legend()
plt.show()