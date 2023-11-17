def f_recur(money):
    if money == 0: return 0
    if money < 0: return float('inf')
    count = float('inf')
    for i in range(len(coin)):
        count = min(count, 1 + f(money-coin[i]))
    return count
coin = [5,10]
print(f_recur(15))
print(f_recur(3))
print(f_recur(30))

#coin = [1,5,10,20,25] => 중첩 부문제 발생으로 런타임 에러남
#print(f(65))

