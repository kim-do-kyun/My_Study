BIN_SIZE = 10
item = [7,5,6,4,2,3,7,5]
n = len(item)
bins = [[] for i in range(n)]   #bins[0] 첫번째 통, bins[1] 두번째 통 ---
remnant = [BIN_SIZE for _ in range(n)]  #각 통의 남는 부분
bin_count = 1

for i in range(n):      #물건 i를 통에 담기
    j = 0
    packed = False
    while j < bin_count:        #기존에 있는 통 j에 물건 i를 담는 경우
        if item[i] <= remnant[j]:
            bins[j].append([i, item[i]])
            remnant[j] -= item[i]
            packed = True
            break
        j+=1
    if not packed:              #새 통에 물건 i를 담는 경우
        bins[j].append([i, item[i]])
        remnant[j] -= item[i]
        bin_count += 1          #통의 수 1증가

print('최초 적합: 총 사용된 통의 수 =',bin_count)
for i in range(bin_count):
    print('통 %d: ' % i)
    for j in range(len(bins[i])):
        print(' 물건 = %d, size = %d ' % (bins[i][j][0], bins[i][j][1]))