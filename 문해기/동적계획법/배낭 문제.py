W = [5, 4, 6, 3]
V = [10, 40, 30, 50]
K = 10
n = len(W)
T = [[0 for _ in range(K+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(K+1):
        if W[i] > j:    #물건 i가 j보다 무거우면
            T[i][j] = T[i-1][j] #물건을 담지 않는다
        else:
            T[i][j] = max(T[i-1][j], V[i] + T[i-1][j-W[i]]) #물건 i를 담지 않는 것과 담는 것 중 가치 큰 경우 선택

print('최대 가치:', T[n-1][K])