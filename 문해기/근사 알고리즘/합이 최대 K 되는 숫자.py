def filtering(A, d):
    A.sort()
    F = [A[0]]
    rep_num = A[0]  #첫 숫자를 대표 숫자로
    for j in range(1, len(A)):
        if A[j] > (rep_num * (1 + d)):
            F.append(A[j])      #A[j]가 대표 숫자*(1+delta)보다 크면 남긴다
            rep_num = A[j]
    return F

S = [-1, 1110, 1008, 1250, 1006]    #입력, s[0]은 사용 안함
K = 2500
n = len(S)
epsilon = 0.4
delta = epsilon/(2*n)       #delta 계산
T = [[0] for _ in range(n)]
for i in range(1, n):
    T[i] = list(set(T[i-1]) | set([x+S[i] for x in T[i-1]]))  #T[i-1]과 T[i-1] + S[1]를 합병 그리고 중복된 숫자 제거
    T[i] = filtering(T[i], delta)                             #대표 숫자만 추출하기 위해
    T[i] = [x for x in T[i] if x <= K]                        #k보다 큰 숫자 제거

print('마지막 숫자 리스트:', T[n-1])
print('근사해 =', max(T[n-1]))