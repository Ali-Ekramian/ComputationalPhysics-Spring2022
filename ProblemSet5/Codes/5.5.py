import numpy as np
import matplotlib.pyplot as plt
import random

N=100

def last_non_zero(arr):
    for oo in range(len(arr)-1,-1,-1):
        if arr[oo]!=0:
            return arr[oo]
    return 0

R_AVG=[]
STD=[]
VAR=[]
T=[]
t=0
n=0
while n<=N:
    final_x=[]
    final_y=[]
    R=[]
    for j in range(100):
        x=np.zeros(N)
        y=np.zeros(N)
        for a in range(n):
            rnd=random.random()
            #print(rnd)
            if rnd<0.25:
                x[a]=x[a-1]+1
                y[a]=y[a-1]
            elif 0.25<rnd<0.5:
                x[a]=x[a-1]-1
                y[a]=y[a-1]
            elif 0.5<rnd<0.75:
                y[a]=y[a-1]+1
                x[a]=x[a-1]
            else:
                y[a]=y[a-1]-1
                x[a]=x[a-1]
            #print('x = ',x)
            #print('y = ',y)
        final_x.append(last_non_zero(x))
        final_y.append(last_non_zero(y))
        #print('final x = ',final_x,"\n",'final y = ',final_y)
    for m in range(len(final_x)):
        r=(final_x[m]**2)+(final_y[m]**2)
        R.append(r)
    print("R = ",R)
    R_av=(sum(R)/len(R))**0.5
    R_AVG.append(R_av)
    print("R AVG = ",R_AVG)
    T.append(t)
    t+=5
    n+=5
del R_AVG[0]
del T[0]
log_R=np.log10(R_AVG)
log_T=np.log10(T)
plt.plot(log_T,log_R,'bo')
fit_av=np.polyfit(log_T,log_R,1)
m_av,b_av=fit_av[0],fit_av[1]
print("slope for log <r(t)> : "  ,m_av,"// y intersept for log <r(t)> : ",b_av)
plt.plot([0,log_T[-1]],[b_av,(m_av*log_T[-1])+b_av],color='blue',label=r'$ \sqrt{\langle r(t)^2 \rangle}  $')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel(r'$\sqrt{\langle r(t)^2 \rangle} $')
plt.legend()
plt.show()
