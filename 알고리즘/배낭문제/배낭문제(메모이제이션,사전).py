def f(n,M):
    if (n,M) in memo: return memo[(n,M)]
    if n == 0 or M == 0: return 0
    if M < w[n-1]: memo[(n,M)] = f(n-1, M)
    else: memo[(n,M)] = max(f(n-1,M), p[n-1]+f(n-1,M-w[n-1]))
    return memo[(n,M)]

M,w,p = 5, [3,2,2], [100,200,300]
memo = {}
print(f(len(w),M))
print(memo)

M, w, p = 70, [1]*50, [1]*50    #중첩 부문제 발생x 재귀에서 안되는거 돌아감
print(f(len(w),M)) 