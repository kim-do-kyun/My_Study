def ft(curSum, sumLeft, i):
    if curSum == T:
        L=[]
        for k in range(i):
            if x[k] == 1: L.append(s[k])
        print(L)
        return
    if i==N: return
    if curSum+s[i] > T or curSum+sumLeft < T: return
    x[i] = 1
    ft(curSum+s[i], sumLeft-s[i], i+1)
    x[i] = 0
    ft(curSum, sumLeft-s[i], i+1)

s = [2,4,5,6]
N = len(s)
T = 10
x = [0]*N
curSum = 0
sumLeft = sum(s)
s.sort()
ft(curSum, sumLeft, 0)