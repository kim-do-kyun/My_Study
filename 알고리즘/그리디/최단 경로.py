n = 8
start = 0   #출발점
graph = [[]] * n
graph[0] = [[1,3],[3,5],[4,6]]
graph[1] = [[2,3],[3,1],[5,4]]
graph[2] = [[3,7]]
graph[3] = [[4,4],[5,1]]
graph[4] = [[5,8],[6,1]]
graph[5] = [[2,6],[7,10]]
graph[6] = [[5,9],[7,1]]
graph[7] = []

included = [False for _ in range(n)]    #경로 확정되면 True
distance = [float('inf') for _ in range(n)] #출발점으로부터 각 정점까지의 거리
distance[start] = 0
previous = [-1 for _ in range(n)]   #최단 경로를 추출하기 위함
previous[start] = 0

for k in range(n):
    m = -1
    min_value = float('inf')
    for j in range(n):
        if not included[j] and distance[j] < min_value:
          min_value = distance[j]
          m = j
    included[m] = True
    for w, wt in graph[m]:
        if not included[w] and distance[m] + wt < distance[w]:
            distance[w] = distance[m] + wt
            previous[w] = m

print('정점 %1d으로부터의 최단 거리 '%start)
for i in range(n):
  print('[%d, %d]=%3d' %(start, i, distance[i]))
print()
print('정점 0으로부터의 최단 경로')
for i in range(n):
  back = i
  print(back, end='')
  while back != 0:
    print('<-',previous[back], end='')
    back = previous[back]
  print()

