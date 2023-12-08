#크키 N 집합 내 원소 선택 조합 출력
#ft(i) -> 인덱스 i 위치 원소 선택 / 미선택 상태 생성
def ft(i):
    if i==N:
        print(x)
        return
    x[i] = 0
    ft(i+1)
    x[i] = 1
    ft(i+1)

x = [0,0,0]
N = len(x)
print('크기 N 집합 내 원소 선택 조합 출력')
ft(0)
print('===========')

#모든 부분집합 출력
def ft(i):
    if i==N:
        L=[]
        for i in range(N):
            if x[i] == 1: L.append(s[i])
        print(x,L)
        return
    x[i]=0
    ft(i+1)
    x[i]=1
    ft(i+1)

s = [9,5,3]
N = len(s)
x = [0]*N
print('모든 부분집합 출력')
ft(0)
print('===========')

#부분집합의 합(subset sum)
#원소의 합이 T인 부분집합 출력
def ft(i):
    if i==N:
        L=[]
        for i in range(N):
            if x[i]==1: L.append(s[i])
        if sum(L) == T: print(x,L)
        return
    x[i]=0
    ft(i+1)
    x[i]=1
    ft(i+1)

s = [2,3,7,9]
N = len(s)
x = [0]*N
T = 12
print('부분집합의 합')
ft(0)