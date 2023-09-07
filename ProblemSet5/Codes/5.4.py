import numpy as np
import matplotlib.pyplot as plt
import random
arr=np.zeros((100,23))
arr[0][11]=1
p=0.5
q=1-p
for i in range(1,20):
    for j in range(1,22):
        arr[i][j]=(arr[i-1][j+1]*q)+(arr[i-1][j-1]*p)
    arr[i][0]+=arr[i-1][1]*q
    arr[i][22]+=arr[i-1][21]*p

for row in arr:
    for elem in row:
        print('{:.6f}'.format(elem), end=' , ')
    print()