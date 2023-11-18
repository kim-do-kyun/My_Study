def f(n,M):
    if memo[n][M] != -1: return memo[n][M]
    if n ==0 or  M == 0: return 0
    if M < w[n-1]: memo[n][M] = f(n-1,M)
    else: memo[n][M] = max(f(n-1,M), p[n-1] + f(n-1, M-w[n-1]))
    return memo[n][M]

M,w,p = 5,[3,2,2],[100,200,300]
memo = []
for i in range(len(w)+1): memo.append([-1]*(M+1))   #리스트 저장소생성및 초기화
print(memo)
print(f(len(w),M))
print(memo)