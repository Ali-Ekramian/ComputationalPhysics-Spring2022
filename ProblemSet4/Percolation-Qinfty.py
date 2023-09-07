import numpy as np
import matplotlib.pyplot as plt
L=10
p=0.0
Q=[]
pr=[]
perc_pr=[]
for gg in range(20):
    #print(p)
    perc_arr=[]
    number1_pr=[]
    for ss in range(100):
        mx=np.random.rand(L,L+2)
        color=np.zeros((L,L+2))
        #print(mx)
        for i in range(len(color)):
            for j in range(len(color[i])):
                if j==0 or j==L+1:
                    color[i][j]=1
        for i in range(len(mx)):
            for j in range(len(mx[i])):
                if j==0 or j==L+1:
                    mx[i][j]=1
                elif mx[i][j]<=p:
                    mx[i][j]=1
                else:
                    mx[i][j]=0
        #print(mx)
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
        #print("\n",color)
        for i in range(L):
            if color[i][L]==1:
                perc=1
                break
            else:
                perc=0
        #print("\n",perc)
        perc_arr.append(perc)
        number1=np.count_nonzero(color==1)-(2*L)
        #print("\n",number1)
        non_zero=np.count_nonzero(color!=0)-(2*L)
        if non_zero==0:
            number1_pr.append(0)
        else:
            number1_pr.append(number1/non_zero)
        #print("\n",number1_pr)
    av_number1=sum(number1_pr)/len(number1_pr)
    Q.append(av_number1)
    print("\n",Q)
    av_perc=sum(perc_arr)/len(perc_arr)
    pr.append(p)
    perc_pr.append(av_perc)
    p+=0.05
    #print(perc_pr)

#plt.plot(pr,perc_pr,'ro')
plt.plot(pr,Q,'bo')
plt.show()
#plt.plot(pr,perc_pr,'bo')
#plt.show()
#plt.imshow(color, cmap='Set1_r')
#plt.show()
#plt.imshow(mx, cmap='viridis_r')
#plt.show()
