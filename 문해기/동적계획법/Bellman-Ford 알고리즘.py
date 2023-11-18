INF = float('inf')
graph = [[INF, 3, 4, INF, INF, INF, INF],
         [INF, INF, INF, 1, INF, INF, INF],
         [INF, INF, INF, INF, 2, INF, INF],
         [INF, INF, INF, INF, 4, -1, INF],
         [INF, -4, INF, INF, INF, INF, 3],
         [INF, INF, INF, INF, INF, INF, 1],
         [INF, INF, INF, INF, INF, INF, INF]]
n = len(graph)

start = 0   #출발점
distance = [INF for _ in range(n)]  #출발점으로부터의 거리
distance[start] = 0
previous = [-1 for _ in range(n)]   #최단 경로를 추출하기 위함
previous[start] = 0
for k in range(n-1):    #n-1회 실행
    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF:  #간선이있을때
                if distance[j] > distance[i] + graph[i][j]:  #간선완화
                    distance[j] = distance[i] + graph[i][j]
                    previous[j] = i     #i 덕분에 j까지의 거리가 단축된 것을 기록
#출력
print('정점 %1d으로부터의 최단 거리 '%start)
for i in range(n):
    print('[%d, %d]=%3d'%(start,i,distance[i]))
print()
print('정점 0으로부터의 최단 경로')
for i in range(n):
    back = i
    print(back, end='')
    while back != 0:
        print('<-',previous[back], end='')
        back = previous[back]
    print()