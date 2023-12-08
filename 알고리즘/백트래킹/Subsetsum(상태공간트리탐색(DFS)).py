def ft(i):
    if i==N:
        L=[]
        for i in range(N):
            if x[i]==1: L.append(s[i])
        if sum(L)==T: print(x,L)
        return
    x[i] = 0
    ft(i+1)
    x[i] = 1
    ft(i+1)

s = [2, 3, 7, 9]
N, T = len(s), 12
x = [0]*N
ft(0)