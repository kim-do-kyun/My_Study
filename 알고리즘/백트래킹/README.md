# 백트래킹(backtracking, 퇴각 검색, 되추적 기법)
* 문제의 해를 구하기 위한 모든 가능한 경우를 <strong>효율적</strong>으로 조사하면서 해를 찾는 알고리즘 설계 방식
* 어떤 조건 검사를 통해 불필요한 경우들을 배제시키는 방식으로 효율성 추구
* 항상 해를 효율적으로 찾을 수 있는 것은 아니며, 대부분의 경우 해를 효율적으로 찾을 수 있음
* 유망하지 않은 노드를 걸러내며 상태공간트리(state space tree)를 탐색하는 기법
* 대게 DFS기반으로 상태공간트리의 루트노드부터 시작하여 각 노드 검사후 유망하지 않으면 
다시 루트노드로 돌아가고 다른 노드로 돌아가고를 반복(이때 돌아가는 과정에서 서브트리가 가지치기(pruning)되는 효과 발생)

## 상태공간트리(state space tree)
* 문제의 해를 찾는 과정에서의 각 상태(state)를 노드로 표현하고, 이전 상태와 다음 상태를 부모노드와 자식노드로 표현한 트리
* ex) S = {2,3,7,9}, T = 12인 경우 {2,3,7}, {3,9}의 두 해가 존재
* ex) S = {2,3,7}, T = 9인 경우 {2,7}의 한 개 해가 존재함
* 완전탐색(전수조사법, exhaustive search, brute-force method) -> 주어진 집합의 모든 가능한 부분집합을 생성하여 그 합이 T가 되는지 검사하는 방법

### Subset sum: 전수조사법
```
<크기 N 집합 내 원소 선택 조합 출력>
def ft(i):
    if i==N:
        print(x)
        return
       x[i] = 0
       ft(i+1)
       x[i] = 1
       ft(i+1)
```
```
<모든 부분집합 출력>
def ft(i):
    if i==N:
        L = []
        for i in range(N):
            if x[i] == 1: L.append(s[i])
        print(x, L)
        return
    x[i] = 0
    ft(i+1)
    x[i] = 1
    ft(i+1)
```
```
<부분집합의 합(subset sum)>
def ft(i):
    if i==N:
        L = []
        for i in range(N):
            if x[i]==1: L.append(s[i])
        if sum(L)==T: print(x, L)
        return
    x[i] = 0
    ft(i+1)
    x[i] = 1
    ft(i+1)
```
```
<Subset sum: 상태공간트리 탐색(DFS)>
def dfs(u, visited):
    visited[u] = 1
    print(u, '=>', end=' ')
    for v in g[u]:
        if visited[v] == 0:
            dfs(v, visited)
          
def dfsMain(g):
    visited = [0]*len(g)
    for u in range(len(g)):
        if visited[u]==0:
            dfs(u, visited)
            print()
```
```
<Subset sum: 백트래킹>
def ft(curSum, sumLeft, i):
    if curSusm == T:
        L = []
        for k in range(i):
            if x[k] == 1: L.append(s[k])
        print(L)
        return
    if i==N: return
    if curSum + s[i] > T or curSum + sumLeft < T: return
    x[i] = 1
    ft(curSum+s[i], sumLeft-s[i], i+1)
    x[i] = 0
    ft(curSum, sumLeft-s[i], i+1)
```