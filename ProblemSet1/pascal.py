def pascal(n):
    num=[[1]]
    for i in range(1,n):
        row=[1]
        for j in range(1,i):
            row.append(num[i-1][j-1]+num[i-1][j])
        row.append(1)
        num.append(row)
    return num

def draw(num):
    maxlen=len(str(num[-1][len(num)//2]))         # Note
    for i in range(len(num)):
        arr=[str(num).center(maxlen) for num in num[i]]
        row=' '.join(arr)
        print('   '*(len(num)-i-1)+row)
draw(pascal(20))

# Note : I got the idea of aligning and centering the pascal triangle 
#        from Internet.

