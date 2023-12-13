U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  #부분 집합들로 커버해야 하는 전체 원소들
S = [{0, 1, 2, 7},        # s0
     {0, 1, 2, 3, 7},     # s1
     {0, 1, 2, 3},        # s2
     {1, 2, 3, 4, 6, 7},  # s3
     {3, 4, 5, 6},        # s4
     {4, 5, 6, 8, 9},     # s5
     {3, 4, 5, 6},        # s6
     {0, 1, 3, 7},        # s7
     {5, 8},              # s8
     {5, 9}]              # s9
set_cover = []            #근사해를 저장

while len(U) > 0:
    max_cover_set = S.index(max(S, key=lambda x : len(U & x)))   #가장 많은 원소를 커버하는 집합 인덱스 찾기
    U = U - S[max_cover_set]        #찾은 집합 원소 제거
    for i in range(len(S)):         #각 부분 집합에서 찾은 집합 원소 제거
        if i != max_cover_set:
            S[i] = S[i] - S[max_cover_set]
    set_cover.append(max_cover_set) #찾은 집합 인덱스를 해에 추가
    S[max_cover_set] = set()        #찾은 집합을 공집합으로
print('집합 커버를 위한 부분 집합 리스트:', set_cover)
