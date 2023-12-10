# Greedy Algorithm
* 최적화(optimization) 문제를 해결하는 문제 방식 중 하나
* 선택 과정에서 모든 데이터를 고려하지 않고 근시안적으로 욕심을 내어 최소(최대)값을 가진 데이터 선택
* 구간 스케줄링, 구간분할, 초 증가순서, 최소 신장 트리, 최단경로, 허프만 코딩

<hr>

### ◎초 증가 순서
* 초 증가 순서(Super Increasing Sequence) : 주어진 숫자들에 대해 각 숫자가 자신보다 앞선 숫자들의 합보다 큰 숫자들
```
입력받은 리스트 정렬 후, 큰수부터 작은 수 순서로 역순으로 실행
리스트의 원소가 K보다 작거나 같으면 결과 값을 저장할 리스트에 추가 
이후 K를 리스트에 저장한 값을 뺀 과정을 K가 0이 될때 까지 반복
==입력에 n개의 숫자가 있어 시간복잡도는 "O(n)"==
```

### ◎최소 신장 트리(Minimum Spanning Tree, MST)
* 트리는 점들이 서로 연결되어 있지만 <strong>사이클</strong>을 가지지 않음
* Spanning Tree(신장트리) : 그래프의 모든 점을 연결하는 트리
* 트리의 특성
  * n개의 점을 가진 그래프의 신장 트리는 n-1개의 간선을 가짐
  * 두 점 사이의 경로는 하나밖에 없다
* 최소 신장 트리(MST) : 간선에 가중치가 부여된 그래프에서 최소 가중치의 합을 가진 신장트리
  * Kruskal 알고리즘
  * Prim 알고리즘
```
<Prim 알고리즘>
임의의 점 하나를 선택하여 T에 넣는다
T 밖에 있는 점 중에서 T에 있는 점과 가장 가까운 점을 T에 추가(이를 n-1회 수행)
==트리에 포함된 정점들을 1회 들어 올릴 때마다 가장 짧게 매달린 점을 찾아야 하므로 최대 O(n)의 시간이 걸림.
따라서 프림 MST 알고리즘의 수행시간은 n X O(n) = O(n²)==
```
```
<Prim 알고리즘 구현>
for k in range(n):
  m = -1
  min_value = float('inf)
  for j in range(n):
    if not included[j] and distance[j] < min_value:   #트리에 포함되지 않고, 가장 짧은 거리일때
      min_value = distance[j] #가장 짧은거리 업데이트
      m = j       #정점 바꾸기
  included[m] = True
  for w, wt in g[m]:
    if not included[w] and wt < distance[w]:  #정점 m에 인접하면서 트리에 포함x 인 점의 distance[]값을 더 작은 값으로 갱신신
      distance[w] = wt
      connected_to[w] = m #나중에 w가 트리에 포함될 때 w가 m과 간선으로 연결된 것을 저장
```

### ◎최단 경로(Shortest path)
* 가중치 그래프의 어느 한 출발점에서 또다른 도착점까지의 최단 경로를 찾는 알고리즘
* 최단 경로 찾는 알고리즘
  * 다익스트라 알고리즘 : 출발점에서 시작, 최단거리가 확정되지 않은 점들 중에서 출발점에서 가장 가까운 점을 추가하고, 추가된 점의 최단 거리를 확정
  * 프림 알고리즘 : 임의의 점에서 시작, 트리에 하나의 정점을 추가할 때 현재 상태의 트리에서가장 가까운 점을 추가
```
<다익스트라 알고리즘>
모든 점이 최단경로가 확정된 점들과 미확정된 점들로 나누고, 한 단계마다 최단 경로가 미확정된 점 중에서 출발점으로부터
가장 가까운 점을 선택, 점들이 확정되는 순서는 최단 거리의 증가 순서
==시작점부터 n회 최단경로가 확정, 간선 완화 또한 O(n)수행 n X (O(n)+O(n)) = O(n²)==
```
```
<다익스트라 알고리즘 구현>
for k in range(n):
  m = -1
  min_value = float('inf)
  for j in range(n):
    if not included[j] and distance[j] < min_value:
      min_value = distance[j]
      m = j
  included[m] = True
  for w, wt in g[m]:
    if not included[w] and distance[m] + wt < distance[w]:
      distance[w] = distance[m] + wt
      previous[w] = m 
```

<br>

### ◎허프만 코딩
* 파일 압축 알고리즘
* 빈도수에 따라서 코드 길이를 가변적으로 부여하면 상당한 압축 효과를 볼 수 있음
* Prefix-free속성 : a가 010이고 b가 0100이면 010이 0100의 앞부분에 나타나서는 안됨.
  즉, 한문자의 코드가 다른 문자의 코드의 앞부분(접두부)과 같아선 안됨
```
<허프만코딩 알고리즘>
[1] 압축할 파일을 스캔하여 각 문자의 빈도수를 계산한다
[2] 각 문자에 대해 문자와 빈도수를 가진 이파리 노드를 만든다
[3] 빈도수가 가장 적은 두 노드의 부모를 만들어 빈도수의 합을 저장한다
[4] if 노드가 하나만 남으면:
        남은 노드를 허프만 트리의 루트로 반환
    else:
        자식이 된 노드들을 제외하고 go to [3]
== (n-1)개의 부모노드를 만들고, 가장 적은 빈도수와 그다음으로 적은 빈도수를 가진 노드를 찾는데 
최소힙 사용시 O(logn)소요 허프만 트리를 만드는 시간은 O(nlogn)==
```
```
<허프만코딩 알고리즘 구현>
def huffman_tree(a):
  h = [[freq, [char, ""]] for char, freq in a]
  heapify(h)
  while len(h) > 1:
    left = heappop(h)
    right = heappop(h)
    for code in left[1:]:
      code[1] = '0' + code[1]
    for code in right[1:]:
      code[1] = '1' + code[1]
    t = [left[0] + right[0]] + left[1:] + right[1:]
    print(t)
    heappush(h, t)
  return h
```