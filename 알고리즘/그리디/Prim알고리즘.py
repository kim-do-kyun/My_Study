# 프림 알고리즘 구현
n = 6   #그래프의 정점 수
#인접 리스트
g = [[]] * n
g[0] = [[1,4],[3,8],[4,2]]
g[1] = [[0,4],[2,9],[4,3]]
g[2] = [[1,9],[3,2],[5,1],[4,7]]
g[3] = [[0,8],[2,2],[4,4],[5,1]]
g[4] = [[0,2],[1,3],[2,7],[3,4]]
g[5] = [[2,1],[3,1]]

included = [False for _ in range(n)]
distance = [float('inf') for _ in range(n)]
distance[0] = 0
connected_to = [-1 for _ in range(n)]

for k in range(n):
    m = -1
    min_value = float('inf')
    for j in range(n):
        if not included[j] and distance[j] < min_value:
            min_value = distance[j]
            m = j
    included[m] = True        
    # print(f'm(정점):{m},min_value(최소가중치):{min_value}')
    # print('included :',included)
    for w, wt in g[m]:
        if not included[w] and  wt < distance[w]:
            distance[w] = wt
            connected_to[w] = m
        # print(f'distance(인접한 정점이{w}일때):',distance)
    # print('connected_to(각 정점에서 연결되는 정점):',connected_to)
    # print('='*60)
print('MST(Prim알고리즘):',end='')
mst_cost = 0
for i in range(1, n):
    print('(%d,%d)'%(i,connected_to[i]),end='')
    mst_cost += distance[i]
print('\nMST의 가중치 :',mst_cost)
        
            