S = [0, 3, 4, 5, 6]
K = 13
n = len(S)-1
T = [[0 for _ in range(K+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(K+1):
        if S[i] > j:
            T[i][j] = T[i -1][j]
        else:
            T[i][j] = max(T[i-1][j], S[i] + T[i-1][j-S[i]])
            
print('T[', n, ',', K, '] =',T[n][K])