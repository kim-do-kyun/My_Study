def is_threatening(i, j):
    for k in range(n):
        if board[i][k] == 1 or board[k][j] == 1:    #같은 행, 같은 열에 있는지 검사
            return True
    for k in range(n):
        for l in range(n):
            if (k+l == i+j) or (k-l == i-j):    #대각선 상에 있는지 검사
                if board[k][l] == 1:
                    return True
    return False

def queen(i):
    if i==n:    #모든 말을 배치했으면
        return True
    for j in range(n):
        if (not(is_threatening(i,j))) and (board[i][j] != 1):
            board[i][j] = 1
            if queen(i+1):  #다음 여왕 말 i+1을 배치하기 위해 순환 호출
                return True
            board[i][j] = 0 #다음 여왕 말 배치하는데 실패했으니 [i][j]를 리셋
    return False

print("여왕 말의 수: ", end='')
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
queen(0)

for x in board:
    print(*x, sep="   ")