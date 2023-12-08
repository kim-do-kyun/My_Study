def promising(i, current_sum, leftover):    #다음 숫자를 고려해도 되는지 검사
    if i == -1:
        return True
    else:
        #조건 검사
        return (current_sum + leftover >= K) and \
            (current_sum == K or current_sum + S[i-1] <= K) #\는 파이썬 문법으로 엔터쳤을때 같은 줄이라고 인식 시키는거(그냥 줄바꿈 단위)

def find_set(i, current_sum, leftover):    #current_sum : 현재까지 포함된 숫자들의 합
    if promising(i, current_sum, leftover): #leftover : 아직 고려 안 된 숫자들의 함
        if current_sum == K:
            return True
        else:
            include[i+1] = True
            if find_set(i+1, current_sum + S[i+1], leftover - S[i+1]):  #S[i+1]을 포함하여 순환 호출
                return True
            include[i+1] = False
            if find_set(i+1, current_sum, leftover - S[i+1]):   #S[i+1]을 포기하여 순환 호출
                return True
    return False

S = [15, 20, 55, 75]
K = 95
n = len(S)
include = [None for _ in range(n)]
if find_set(-1, 0, sum(S)):
    print([S[j] for j in range(n) if include[j]])
else:
    print('답 없음')