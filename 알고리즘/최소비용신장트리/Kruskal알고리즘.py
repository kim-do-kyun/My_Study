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

def kruskal(N, E):
    E.sort(key = lambda e:e[2])     #간선 가중치로 간선들을 오름차순 정렬
    parent, rank = [0]*N, [0]*N
    for i in range(N):
        parent[i] = i
    i, NumEdge, mst, mstSize, cost = 0, len(E), [], 0, 0
    while i<NumEdge and mstSize < N-1:  #미처리 간선 남아있고 아직 신장트리 미발견 시
        u, v, w = E[i]                  #미처리 간선 중 최소비용간선 선택
        if find(u, parent) != find(v, parent):  #MST에 간선 (u,v) 추가로 사이클 형성 검사
            mst.append(E[i])            #MST에 간선 (u,v)추가
            mstSize += 1                #MST 크기 1 증가
            cost += w                   #MST cost 갱신
            union(u,v, parent, rank)    #두 정점 u,v가 속한 집합들을 합집합
        i+=1                            #다음 간선으로 이동
    if mstSize < N-1: return [], -1     #신장 트리 없는경우
    else: return mst, cost

N, E = int(input()), []
for i in range(int(input())):
    u, v, w = input().split()
    E.append((int(u), int(v), float(w)))

print(kruskal(N,E))