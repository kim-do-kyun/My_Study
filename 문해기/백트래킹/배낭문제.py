n = 4
K = 10
p = [54, 40, 30, 10]
w = [3,4,6,5]
maxp = 0
include = [0,0,0,0]
bestset = [0,0,0,0]

#profit : 현재 노드까지의 물건 가치의 합
#weight : 현재 노드까지의 무게의 합
#bound : 현재 노드에서의 한정 값(넣을 수 있는 최대 가치 계산 값)

def promising(i, weight, profit):
    global maxp
    if (weight >= K):   #weight가 목표 K초과 하는지 확인
        return False
    else:
        j = i+1
        bound = profit
        totweight = weight
        #한정값 계산하기
        while j<n and totweight + w[j] <= K:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k<n:
            bound += (K-totweight)*p[k]/w[k]
        return bound > maxp

def knapsackBT(i, profit, weight):
    global bestset
    global maxp
    #weight가 k이하이고 profit이 최대이익보다 크면
    if(weight <= K and profit > maxp):
        maxp = profit
        bestset = include[:]

    #다음으로 진행 가능하면
    if promising(i, weight, profit):
        #다음 노드 포함하여 순환호출
        include[i+1] = 1
        knapsackBT(i+1, profit+p[i+1], weight+w[i+1])
        #다음 노드 포기하여 순환호출
        include[i+1] = 0
        knapsackBT(i+1, profit, weight)

knapsackBT(-1, 0, 0)
print(maxp)
print(bestset)

