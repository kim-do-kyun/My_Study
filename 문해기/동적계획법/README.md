# Dynamic Programming(동적 계획)알고리즘
* 문제를 작은 것(부분 문제)부터 푼다는 점이 분할정복 알고리즘과 비슷함
* 그리디 알고리즘과 같이 최적화 문제를 해결하는 방법

> 동적 계획 알고리즘은 최적 부분 구조(Optimal Substructure)를 지닌 중복된 하위 문제들(Overlapping Subproblems)을 분할 정복으로 풀이하는 문제해결 패러다임
<hr>

### ◎가장 긴 증가 순서
* 일렬로 나열된 숫자중에서 가장 긴 증가 순서를 찾는 알고리즘
* ex) ```[5,2,8,6,4,6,1,9,3] 중 가장 긴 증가 순서는 [2,4,6,9]```
```
주어진 숫자로 그래프 생성, 가장 왼쪽 정점으로부터 하나씩 차례로 정점 i로 들어오는 
간선 <j,i>의 왼쪽 끝 정점 j 까지 계산된 경로중 가장 긴 길이에 1을 더하여 정점 i의 경로의 길이를계산
모든 점을 검사하여 가장 긴 경로를 반환
==첫 단계에서 그래프를 만드는데 이때 간선 수만 해도 최대 n(n-1)/2 즉 그래프 만드는 시간만 O(n²), 다음 단계가 좌에서 우로 각점으로 들어오는 간선에 대한 연산이므로 간선 수와 같음 
O(n²) + O(m) = O(n²)==
```
```
<가장 긴 증가 순서 구현>
for i in range(1, n):
    if g[i] is not None:        #들어오는 간선이 있을때 (없는경우 None)
        max_length = -1 
        for j in g[i]:          #들어오는 각 간선의 끝점 중 가장 긴 것 찾기
            if length[j] > max_length:
                max_length = length[j]
                previous[i] = j
        length[i] = max_length + 1  #자신의 숫자를 길이에 반영
```


### ◎벨만-포드(Bellman-Ford)알고리즘
* 다익스트라 최단 경로 알고리즘의 문제점(다익스트라는 그리디알고리즘)
  * 음수 가중치를 가진 그래프에서 최단경로 못찾음
  * 그리디 알고리즘은 확정된 값에 대해 수정을 허락하지 않음 : 확정된 점에 대한 간선 완화 불가능
* 정점을 0, 1, ..., n-1로 하여 알고리즘 종료 후에 distance[i]가 출발점에서 마지막 점 i까지의 최단 거리를갖는다
* 벨만-포드 알고리즘이 동적 계획 알고리즘인 이유
  * 시작점 자체가 가장 작은 문제
  * 각 정점의 관점에서 간선 완화가 진행되는 과정 그 자체가 작은 것부터 해결하는 방식이라 할 수 있음
```
<벨만-포드 최단 경로 알고리즘>
distance를 ∞로 초기화(float('inf')) 단 distance[start] = 0, start는 출발점
if distance[j] > (distnace[j] + 간선 <i, j>의 가중치):
    distance[j] = distance[j] + 간선 <i, j>의 가중치
    previous[j] = i
이를 n-1외 수행
==간선 완화를 n-1회 시도, 각 간선 완화는 O(1)의 시간이 걸리므로 (n-1) X O(m) = O(nm),
여기서 m은 간선수 아래 구현처럼 인접 행렬을 사용하면 수행시간은 O(n³)==
```
```
<벨만-포드 알고리즘 구현>
for k in range(n-1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF:
                if distance[j] > distance[i] + graph[i][j]:
                    distance[j] = distance[i] + graph[i][j]
                    previous[j] = i
```