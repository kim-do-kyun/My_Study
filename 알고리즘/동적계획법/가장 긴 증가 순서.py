s = [5,2,8,6,4,6,1,9,3]
n = len(s)      #정점 수
g = [None,None,[0,1],[0,1],[1],[0,1,4],None,[0,1,2,3,4,5,6],[1]]
previous = [-1 for _ in range(n)] #증가 순서를 추출
length = [1 for _ in range(n)]  
for i in range(1, n):
    if g[i] is not None:    #들어오는 간선이 있으면
        max_length = -1 
        for j in g[i]:          #들어오는 각 간선의 끝점 중 가장 긴 것 찾기
            if length[j] > max_length:
                max_length = length[j]
                previous[i] = j
        length[i] = max_length + 1      #자신의 숫자를 길이에 반영
    
print('가장 긴 증가 순서의 길이 =',max(length))

k = length.index(max(length))       #가장 긴 증가 순서 길이를 가진 점의 인덱스 찾기
seq = [k]
while previous[k] != -1:
    seq.insert(0, previous[k])            
    k = previous[k]
lis = [s[i] for i in seq]
print('가장 긴 증가 순서 = ', lis)