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
```
```
for i in range(1, n):
    if g[i] is not None:        #들어오는 간선이 있을때 (없는경우 None)
        max_length = -1 
        for j in g[i]:          #들어오는 각 간선의 끝점 중 가장 긴 것 찾기
            if length[j] > max_length:
                max_length = length[j]
                previous[i] = j
        length[i] = max_length + 1  #자신의 숫자를 길이에 반영
```