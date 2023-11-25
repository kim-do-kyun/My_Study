S = 'script'
T = 'scope'
m = len(S)
n = len(T)
E = [[_ for _ in range(n+1)] for _ in range(m+1)]   #편집 거리 저장
for i in range(m+1):    #초기화
    E[i][0] = i
for j in range(n+1):
    E[0][j] = j    

for j in range(1, n+1):
    for i in range(1, m+1):
        if S[i - 1] == T[j - 1]:
            alpha = 0
        else:
            alpha = 1
        E[i][j] = min(E[i - 1][j] + 1, E[i][j - 1] + 1, E[i - 1][j - 1] + alpha)

print(S, '->', T, '의 편집 거리:', E[m][n])

