from heapq import heappush, heappop, heapify

def huffman_tree(a):
    h = [[freq, [char, ""]] for char, freq in a]    #허프만 트리 초기화
    heapify(h)      #최소 힙 만들기
    while len(h) > 1:
        left = heappop(h)
        right = heappop(h)
        for code in left[1:]:       #왼쪽 자식은 0을 맨 앞에 추가
            code[1] = '0' + code[1]
        for code in right[1:]:      #오른쪽 자식은 1을 맨 앞에 추가
            code[1] = '1' + code[1]
        t = [left[0] + right[0]] + left[1:] + right[1:]     #left와 right를 합하여 만든 노드
        print(t)
        heappush(h, t)      #t를 힙에 삽입
    return h

input_freq = [['b',20], ['c', 30], ['d',35], ['e', 40], ['a', 60], ['f', 90]]

h_code = huffman_tree(input_freq)

result = sorted(heappop(h_code)[1:], key=lambda x: x)
for ch, code in result:
    print(ch, ':', code)
