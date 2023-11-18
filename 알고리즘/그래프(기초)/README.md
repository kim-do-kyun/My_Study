# :books:그래프
* <strong>간선(링크)</strong>으로 연결된 <strong>정점(노드)</strong>들의 모음을 표현
* <strong>정점(vertex, node)</strong>들의 집합 V와 <strong>간선(edge, link)</strong>들의 집합 E로 구성 <strong>G = (V, E)</strong>로 표기
  * <strong>무방향 그래프</strong> - 정점과 정점을 연결하는 간선들의 방향이 없는 경우
    * 두 정점 u,v를 연결하는 무방향 간선은 {u,v}로 표기
  * <strong>방향 그래프</strong> - 간선들의 방향이 있는 경우
    * 두 정점 u,v에 대해 u에서 v방향으로 (u,v)로 표기
  * 관습 상 둘다 (u,v)로 표기하지만 무방향 그래프에서는 {u,v}의 의미로 해석해야함
* <strong>용어</strong>
  * 하나의 간선으로 연결된 두 정점들을 <strong>인접(adjacent)</strong>하다고함
  * 두 정점에 연결된 각 정점에 <strong>부속(incident)</strong>된다고함
  * 정점에 부속된 간선의 개수를 해당 정점의 <strong>차수(degree)</strong>라고 함
  * <strong>방향그래프</strong>의 경우 정점에서 나가는 간선의 수를 해당 정점의 <strong>진출차수(out-degree)</strong>라고 하며, 정점으로 들어오는 간선의 수를 해당 정점의 <strong>진입차수(in-degree)</strong>라고 함 
  ※방향그래프에서 정점의 차수는 <strong>입력차수</strong>와 <strong>출입차수</strong>의 합합

* <strong>숲(forest, acyclic undirected graph)</srong> : 사이클이 없는 무방향 그래프
* <strong>자유트리(free tree, acyclic connected undirected graph)</strong> : 사이클이 없는 연결된 무방향 그래프
  