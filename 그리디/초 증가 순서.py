S = list(map(int, input("초 증가 순서 리스트 입력 : ").split()))
K = int(input("K 값 : "))
S.sort()

solution = []
i = len(S) - 1
while K > 0:
    if S[i] <= K:
        solution.append(S[i])
        K -= S[i]
    i -= 1

print(f'선택된 수의 리스트 : {solution}, 리스트 합 : {sum(solution)}')