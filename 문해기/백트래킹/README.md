# Backtracking 알고리즘
* 해를 찾는 과정에서 해를 더 이상 얻지 못하면 바로 직전 상태로 되돌아가서 다른 것을 시도하며 해를 찾는다
* 최적화 문제와 결정 문제(문제에 대한 해의 존재 여부)를 해결
* 해 탐색 순서 : 깊이 우선(Depth First)
  * 깊이 우선 탐색의 보완 : 분기 한정(Branch and Bound)알고리즘
* 탐색을 중단하는 것 : 가지치기(pruning)
* 상태 공간 트리(state space tree) : 가지치기에서 부모노드로 되돌아가서 다른 색을 선택하는 트리
<hr>

### ◎그래프 색칠하기
* 주어진 그래프를 최소의 색으로 인접한 정점들을 서로 다르게 색칠하는 문제
* <strong>상태 공간 트리를 실제로 만들지 않는다</strong>
```
<그래프 색칠하기 알고리즘>
[1] 정점 0을 하나의 색으로 칠한다
[2] 모든 점이 색칠될 때까지 다음 점이 이미 색칠된 점과 인접하면, 인접한 점들의 색과 다른 색을 선택
단, 주어진 K에 대해 색칠에 실패하면 K를 1증가 후 처음부터 다시 알고리즘 수행
```
```
<그래프 색칠하기 구현>
def valid(i):
  for j in range(n):  
    if g[i][j] and color[i] == color[j] and (color[i] != -1):
      return False #i와 j가 인접하고, -1이 아닌 같은 색으로 칠해졌으면 False반환
  return True
  
def coloring(i):
  if i == n:    #모든 정점의 색칠이 완료되면 색칠 결과 출력
    print('색칠 결과:',color)
    return True
  
  for c in range(K):
    color[i] = c
    if valid(i):    #정점 i를 c로 칠해도 되는지 확인하기 위해 valid(i)호출
      if coloring(i + 1):   #다음 점, 즉 i+1을 칠하기 위해 순환 호출
        return True
  return False
```
<br>

### ◎여왕 말 문제(n-Queens Problem)
* 여왕 말이 같은 열, 같은 행, 같은 대각선상에 서로 놓이지 않도록 n X n 장기판에 n개의 퀸을 배치하는 문제
```
<여왕 말 백트래킹 알고리즘>
[1] Q를 (0,0)부터 놓기 시작하여 다음 Q를 서로 위협하지 않도록 배치한다
[2] 배치할 수 없으면, 직전 Q의 위치를 다음 칸으로 이동하여 다시 시도
다음 칸이 없는 경우에는 위층의 Q를 다음 칸으로 이동하여 시도(배치할 수 있으면 1, 없으면 0)
```
* 최초에 queen(0)으로 호출되어 모든 여왕 말을 배치하면 종료
* is_threatening함수는 (i, j)에 여왕 말을 놓았을 때 상하좌우, 대각선, 역대각선 상을 검사해 문제 없으면 True
* queen 함수는 순환호출, i==n이면 종료 그렇지 않으면 for-루프에서 (i, 0), (i, 1),--(i, n-1)까지 검사해 여왕말 i를 배치할 수 있으면 queen(i+1)로 순환호출
```
<여왕 말 백트래킹 구현>
def is_threatening(i, j):
  for k in range(n):
    if board[i][k] == 1 or board[k][j] == 1:  #같은 행, 같은 열에 있는지 검사
      return True
  for k in range(n):
    for l in range(n):
      if (k+l == i+j) or (k-l == i-j):
        if board[k][l] == 1:
          return True
  return False
  
def queen(i):
  if i == n: #모든 말을 배치했으면
    return True
  for j in range(n):
    if (not(is_threatening(i, j))) and (board[i][j] != 1):
      board[i][j] = 1   #배치할 수 있으니까 1
      if queen(i + 1):  #그 다음 여왕말 검사
        return True
      board[i][j] = 0   #배치할 수 없으므로 0
  return False
```
<br>

### ◎합이 K되는 숫자 백트래킹
* 모든 조합을 검사하는 것과 근본적으로 같은 방법
* 체계적으로 해를 찾으면서 해가 될 수 없는 조합을 건너뛸 수 있다
```
<합이 K되는 숫자 백트래킹 알고리즘>
[1] 주어진 숫자들을 증가 순으로 정렬한다(오름차순 정렬)
[2] 순서대로 숫자를 선택하는 경우, 포기하는 경우로 나누어 상태공간트리의 노드를 만듬 만들수 없으면 부모노드로 돌아가 다른 노드를 선택
[3] 위에서 만든 노드에서 해를 찾으면 종료, 아니면 다시 [2]를 수행
```
* 가지치기(punning)
  * 입력을 정렬하는 이유 : 자식 노드를 만들 때 다음 숫자를 추가한 합이 K를 초과하면 그 이후의 숫자는 다음 숫자보다 커 만들어진 노드로부터
  아래로 더 이상 탐색해도 해가 없기 때문
  * 탐색 중단 : 가지치기(punning)
  * 또한 탐색 중 남은 숫자들을 다 더해도 K보다 작은 경우에도 가지치기 수행
```
<합이 K되는 숫자 백트래킹 구현>
def promising(i, current_sum, leftover):  #다음 숫자를 고려해도 되는지 검사
  if i == -1:
    return True
   else:
    return (current_sum + leftover >= K) and (current_sum == K or current_sum + S[i-1] <= K) #조건검사
    
def find_set(i, current_sum, leftover):     #current_sum : 현재까지 포함된 숫자들의 합
  if promising(i, current_sum, leftover):   #leftover : 아직 고려 안 된 숫자들의 합
    if current_sum == K:
      return True
    else:
      include[i+1] = True
      if find_set(i+1, current_sum + S[i+1], leftover - S[i+1]):    #S[i+1]을 포함하여 순환 호출
        return True
      include[i+1] = False
      if find_set(i+1, current_sum, leftover - S[i+1]):   #S[i+1]을 포기하여 순환 호출
        return True
  return False
```

### ◎배낭문제
* 동적 계획 알고리즘보다 백트래킹으로 푸는게 더 성능이 좋음
* 깊이우선탐색보다 최선 우선(Best-first)탐색을 하는것이 더 빠르게 해를 찾을 수 있음
* 노드의 한정값(bound) : 그 노드가 얼마나 해에 가까운지를 알려주는 수치
```
<배낭 문제 알고리즘>
[1] 단위 무게 당 가치를 기준으로 물건들을 감소 순으로 정렬
[2] 상태 공간 트리의 루트를 만든다
[3] 물건을 포함하여 자식 노드와 포기한 자식 노드를 만들고 각각 bound를 계산한다
[4] 상태 공간 트리의 이파리 중에서 가장 큰 bound를 가진 노드를 선택. 만일 남은 이파리들이 현재까지 찾ㅇ느
가장 큰 가치보다 작은 bound를 갖고 있으면 알고리즘 종료
[5] go to [3]
```
```
<배낭 문제 구현>
def promising(i, weight, profit):
  global maxp
  if (weight >= K):
    return False
  else:
    j = i+1
    bound = profit
    totweight = weight
    while j < n and totweight + w[j] <= K:
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
  if(weight <= K and profit > maxp):
    maxp = profit
    bestset = include[:]
    
  if promising(i, weight, profit):
    include[i+1] = 1
    knapsackBT(i+1, profit+p[i+1], weight+w[i+1])
    include[i+1] = 0
    knapsackBT(i+1, profit, weight)
```
