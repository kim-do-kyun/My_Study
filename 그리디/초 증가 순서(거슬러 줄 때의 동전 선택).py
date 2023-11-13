coin = [1,5,10,50,100,500]
K = int(input("거슬러줄 액수 : "))
solution = []

def changeCoin(coin,K):
    coin.sort(reverse = True)
    i = 0
    while K > 0:
        if coin[i] > K:
            i += 1
            continue
        elif coin[i] <= K:
            solution.append(coin[i])
            K -= coin[i]
            i += 1
    return solution
print(changeCoin(coin,K))