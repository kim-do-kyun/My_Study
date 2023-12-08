def ft(i):
    if i==N:
        print(x)
        return
    x[i]=0  #원소 미선택
    ft(i+1)
    x[i]=1  #원소 선택
    ft(i+1)
    x[i]=0  #불필요

x = [0,0,0]
N = len(x)
ft(0)