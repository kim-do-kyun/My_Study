# 최소 비용 신장 트리(Minimum-Cost Spanning Tree, MST)
* 신장 트리(spanning tree)
  * 그래프 G의 모든 정점을 포함하면서 G내 간선들로만 구성된 트리
  * 신장트리는 n개 노드로 구성된 그래프 내 모든 n개 정점을 n-1개 간선으로 연결하는 트리
  * 하나의 그래프에는 여러 신장트리 존재 가능
* 최소 비용 신장 트리(minimum cost spanning tree,minimum spanning tree, MST)
  * 최소 비용을 갖는 신장트리
  * 신장트리의 비용 -> 가중치가 부여된 무방향 그래프 G의 신장트리 T의 비용은 T내 간선들의 가중치의 합으로 정의
  * 그리디 알고리즘 사용

### 최소비용신장트리 : Kruskal 알고리즘
* 개요 : 최초 공백 최소비용신장트리 T와 그래프 간선 집합 E로부터 시작하여, E로 부터 최소비용간선 e를 삭제 추출한 후, e를 T에 추가한다고 가정했을때 T내 사이클이 만들어지지않으면 e를 T에 실제로 추가하는 잡업을 T가 신장트리가 될 때까지 반복
```
<최소 비용 간선 결정>
- 최초 E를 O(e log e) 시간에 정렬하거나 
- O(e) 시간엔 최소힙 구성, 최소힙에서 최소비용간선을 O(log e) 시간에 삭자
* 사이클감지 : Union-find 연산 활용
```
#### 서로소집합(disjoint set)
* 서로소인 동적 집합들의 모음을 표현
* 연산  
  * MAKE-SET(x) => x가 유일한 원소인 새로운 집합 {x}를 생성
  * UNION(x, y) => 원소 x가 속한 집합 Sx와 원소 y가 속한 집합 Sy의 합집합 Sx U Sy수행
  * FIND(X) => 원소 X가 속한 집합의 대표 원소를 반환
* Disjoint sets을 Disjoint-set forest로 구현
  * 서로소인 각 집합을 하나의 루트 트리(rooted tree)로 표현
  * 효율성을 위해 더 많은 노드를 갖는 트리의 루트가 더 적은 노드를 갖는 트리 루트의 parent가 되도록 합집합 수행
```
<단순 find>
* 원소 i의 parent 링크를 따라 올라가면서 발견되는 루트 원소 id를 반환

{0,1,2,3},{4}
def find(i, parent):          find(0) => 3
  while i!= parent[i]:   =>   find(1) => 3
    i = parent[i]             find(2) => 3
  return i                    find(3) => 3
                              find(4) => 4
```
```
<단순 union>
* 원소 x가 속한 집합과 원소 y가 속한 집합의 합집합 수행(find(x)와 find(y)가 같으면 같은 집합이므로 수행 불필요, 다르다면 x가 속한 집합의 대표원소의 부모를 y가 속한 집합의 대표원소로 설정)

def find(i, parent):
  while i != parent[i]:
    i = parent[i]
  return i

def union(i, j, parent):
  i = find(i, parent)
  j = find(j, parent)
  if i==j: return
  parent[i] = j
```
```
<union by rank>
* 두 트리 합집합 시, 더 큰 rank를 갖는 트리 루트 노드가 더 작은 rank를 갖는 트리 루트 노드의 부모 노드가 되도록 합집합 수행(두 트리의 루트들의 rank가 같은 경우 합집화된 트리 루트의 rank 1 증가)

def find(i, parent):
  while i != parent[i]:
    i = parent[i]
  return i

def union(i, j, parent, rank):
  i = find(i, parent)
  j = find(j, parent)
  if i==j: return
  if rank[i] < rank[j]: parent[i] = j
  elif rank[i] > rank[j]: parent[j] = i
  else:
    parent[i] = j
    rank[j] += 1
```
```
<경로 압출 기반 find 연산(find by path compression)>
* 경로압축(path compression) : 루트노드까지 올라가는 경로 상의 각 노드의 부모노드를 루트로 갱신

def find(i, parent):
  if i != parent[i]:
    parent[i] = find(parent[i], parent)
  return parent[i]
```
