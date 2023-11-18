def f(money):
    if memo[money] != -1: return memo[money]
    if money == 0: return 0
    if money < 0: return float('inf')
    count = float('inf')
    coinUsed = -1
    for i in range(len(coin)):
        new_count = 1 + f(money-coin[i])    #각 동전 한개를 사용한 경우 이전보다 더 적은 최소동전수가 주어진다면 사용된 동전 액면가를 저장
        if new_count < count:
            count = new_count
            coinUsed = coin[i]
    memo[money] = count
    P[money] = coinUsed #최소 선택해야할 동전의 액면가 저장
    return count

def printCoinChange(money):
    if P[money] == 1:
        print('교환 불가')
        return
    while money > 0:
        print(P[money])
        money -= P[money]
        
coin, money = [5,10], 25
memo = [-1]*(money+1)
P = [-1]*(money+1)
print(f(money))
printCoinChange(money)