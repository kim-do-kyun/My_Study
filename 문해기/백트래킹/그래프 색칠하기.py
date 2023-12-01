def valid(i):
    for j in range(n):
        if  g[i][j] and color[i] == color[j] and (color[i] != -1):
            #i와 j가 인접하고, -1이 아닌 같은 색으로 칠해졌으면 False 반환
            return False
    return True

def coloring(i):
    if i == n:  #모든 정점의 색칠이 완료되면 색칠 결과 출력
        print('색칠 결과:',color)
        return True

    for c in range(K):
        color[i] = c
        if valid(i):
            if coloring(i + 1):
                return True
    return False

g = [[0, 1, 0, 1, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [0, 1, 0, 1, 0, 0],
     [1, 1, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 1],
     [1, 1, 0, 0, 1, 0]]
n = len(g)
K = 3   #색은 0, 1, 2
color = [-1 for i in range(n)]  #각 정점의 색을 -1로 초기화
if not coloring(0):
    print('색칠 할 수 없음')