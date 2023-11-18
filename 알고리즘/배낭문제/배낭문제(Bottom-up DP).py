def f(NumItem, Capacity, w, p):
    dp = []
    for i in range(NumItem+1):
        dp.append([-1]*(Capacity+1))
    for n in range(NumItem+1):
        for M in range(Capacity+1):
            if n == 0 or M == 0: dp[n][M] = 0
            elif M < w[n-1]: dp[n][M] = dp[n-1][M]
            else: dp[n][M] = max(dp[n-1][M], p[n-1] + dp[n-1][M-w[n-1]])
    return dp[NumItem][Capacity]

# M,w,p = 5, [3,2,2], [100,200,300]
# print(f(len(w),M,w,p))

# M,w,p = 7, [4,6,4,3,5], [7,13,8,6,12] 백준12865
# print(f(len(w),M,w,p))