import numpy as np
import matplotlib.pyplot as plt
L=10
p=0.3

mx=np.random.rand(L,L+2)
color=np.zeros((L,L+2))
print(mx)
for i in range(len(color)):
    for j in range(len(color[i])):
        if j==0 or j==L+1:
            color[i][j]=1
print(color,"\n")

for i in range(len(mx)):
    for j in range(len(mx[i])):
        if j==0 or j==L+1:
            mx[i][j]=1
        elif mx[i][j]<=p:
            mx[i][j]=1
        else:
            mx[i][j]=0
print(mx)
k=1

for j in range(1,L+1):
    for i in range(L):
        if i==0:
            if mx[i][j]==1:
                if mx[i][j-1]==1:
                    color[i][j]=color[i][j-1] 
                else:
                    color[i][j]=k+1
                    k+=1
            else:
                continue
        else:
            if mx[i][j]==1:
                if mx[i][j-1]==1 and mx[i-1][j]==1:
                    color[i][j]=min(color[i][j-1],color[i-1][j])
                    for m in range(1,j+1):
                        for n in range(L):
                            if color[n][m]==max(color[i][j-1],color[i-1][j]):
                                color[n][m]=min(color[i][j-1],color[i-1][j])
                elif mx[i][j-1]==1:
                    color[i][j]=color[i][j-1]
                elif mx[i-1][j]==1:
                    color[i][j]=color[i-1][j]
                else:
                    color[i][j]=k+1
                    k+=1
            else:
                continue
print("\n",color)
for i in range(L):
    if color[i][L]==1:
        perc=1
        break
    else:
        perc=0
print("\n",perc)
for i in range(len(color)):
    for j in range(len(color[i])):
        if color[i][j]==1:
            color[i][j]=20

plt.imshow(color, cmap='Paired_r')
plt.show()
plt.imshow(mx, cmap='viridis_r')
plt.show()
