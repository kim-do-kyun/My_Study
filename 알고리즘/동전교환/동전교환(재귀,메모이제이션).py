#재귀적 구현
def f_recur(money):
    if money == 0: return 0
    if money < 0: return float('inf')
    count = float('inf')
    for i in range(len(coin)):
        count = min(count, 1 + f_recur(money-coin[i]))
    return count
coin = [5,10]
print('[재귀적 구현]')
print(f_recur(15))
print(f_recur(3))
print(f_recur(30))

#coin = [1,5,10,20,25] => 중첩 부문제 발생으로 런타임 에러남
#print(f(65))

#Top-down 메모이제이션 기반 구현(사전 사용)
def f_memo_dic(money):
    if money in memo: return memo[money]    #money를 거슬러 주는 f_memo_dic가 이전에 계산되었다면 그 값을 바로 반환
    if money == 0: return 0
    if money < 0: return float('inf')
    count = float('inf')
    for i in range(len(coin)):
        count = min(count, 1 + f_memo_dic(money-coin[i]))
    memo[money] = count     #계산된 f_memo_dic값을 이후 재사용을 위해 반환 전에 보관 
    return count

coin, memo = [5,10], {}
print('[Top-down 메모이제이션(사전) 구현]')
print(f_memo_dic(25))
print(memo)

#Top-down 메모이제이션 기반 구현(리스트 사용)
def f_memo_list(money):
    if memo[money] != -1: return memo[money]
    if money == 0: return 0
    if money < 0: return float('inf')
    count = float('inf')
    for i in range(len(coin)):
        count = min(count, 1 + f_memo_list(money-coin[i]))
    memo[money] = count
    return count

coin = [5,10]
money = 25
memo = [-1]*(money+1)
print('[Top-down 메모이제이션(리스트) 구현]')
print(f_memo_list(money))