n = 6   #그래프 정점 수
graph = [[]] * n
graph[0] = [[1,4],[3,8],[4,2]]
graph[1] = [[0,4],[2,9],[4,3]]
graph[2] = [[1,9],[3,2],[5,1]]
graph[3] = [[0,8],[2,2],[4,4],[5,1]]
graph[4] = [[0,2],[1,3],[2,7],[3,4]]
graph[5] = [[2,1],[3,1]]

included = [False for _ in range(n)]    #트리에 포함되면 True로
distance = [float('inf') for _ in range(n)] #트리의 정점에서 각 정점까지의 거리
distance[0] = 0
connected_to = [-1 for _ in range(n)]   #트리의 간선을 추출하기 위함

for k in range(n):
    m = -1  #정점
    min_value = float('inf')
    for j in range(n):
        if not included[j] and distance[j] < min_value: #트리에 포함되지 않고, 가장 짧은 거리일때
            min_value = distance[j] #가장 짧은거리 업데이트
            m = j   #정점 바꾸기
    included[m] = True
    for w, wt in graph[m]:
        if not included[w] and wt < distance[w]:    #정점 m에 인접하면서 트리에 포함x인 점의 distance[]값을 더 작은 값으로 갱신
            distance[w] = wt
            connected_to[w] = m #나중에 w가 트리에 포함될 때 w가 m과 간선으로 연결된것을 저장

print('MST: ',end='')
mst_cost = 0
for i in range(1, n):
    print('(%d %d)' % (i, connected_to[i]), end='')
    mst_cost += distance[i]
print('\nMST의 가중치 : ',mst_cost)