def f(n, M):
    if n==0 or M==0: return 0
    if M < w[n-1]: return f(n-1,M)
    return max(f(n-1,M), p[n-1]+f(n-1, M-w[n-1]))

M = 30
w = [5,10,25]
p = [100,300,500]
print(f(len(w),M))

# M, w, p = 70, [1]*50, [1]*50    #중첩 부문제 발생
# print(f(len(w),M)) 