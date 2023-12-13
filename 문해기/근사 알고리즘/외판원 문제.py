tree = [[1],[0,3],[3],[1,2,4,5],[3],[3,6],[5]]  #MST
n = len(tree)
INF = float('inf')
g = [[0, 2, INF, 5, INF, INF, 5],
     [2, 0, 5, 3, INF, 6, 8],
     [INF, 5, 0, 1, 5, INF, INF],
     [5, 3, 1, 0, 2, 2, INF],
     [INF, INF, 5, 3, 0, 6, 10],
     [INF, 6, INF, 2, 6, 0, 3],
     [5, 8, INF, INF, 10, 3, 0]]
visited = [False for _ in range(n)]
path = []

def dfs(v):
    visited[v] = True
    path.append(v)      #처음 방문할 때 경로에 추가
    for w in tree[v]:
        if not visited[w]:
            dfs(w)      #v에 인접한 w로 순환 호출
            path.append(v)  #되돌아 나올때 경로에 추가

dfs(0)
print('트리 방문 순서:',path)
s = []
for vertex in path:
    if vertex not in s:     #중복 방문 제거
        s.append(vertex)
s.append(0)
print('TSP 경로:', s)