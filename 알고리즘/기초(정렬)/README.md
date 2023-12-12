# 정렬
## 선택정렬(selection sort)
* 정렬 방법 -> 비어 있는 정렬 리스트 S와 비정렬 리스트 U가 주어질 때, U 내 최소값을 선택하여
S의 오른쪽 끝으로 이동, 이 작업을 U가 공백 리스트가 될때까지 반복
* 비교 연산 기준 시간복잡도 T(n) = (n-1) + (n-2) + -- + 2 + 1 = n(n-1)/2 = O(n²)
```
def selectionSort(v):
    for i in range(len(v)):
        minIndex = i
        for j in range(i+1, len(v)):
            if v[j] < v[minIndex]:
                minIndex = j
        t = v[i]
        v[i] = v[minIndex]
        v[minIndex] = t
```

<br>

## 삽입정렬(insertion sort)
* 정렬 방법 -> 비어 있는 정렬 리스트 S와 비정렬 리스트 U가 주어질 때, U로부터 하나의 값을 제거하여 
S 내 올바른 위치에 삽입하는 작업을 U가 공백 리스트가 될 때까지 반복
* 이동 연산 횟수 기준 시간복잡도 T(n) = 1 + 2 + -- + (n-2) + (n-1) = n(n-1)/2 = O(n²)
```
def insertionSort(v):
    for i in range(1, len(v)):
        key = v[i]
        j = i - 1
        while j>=0:
            if v[j] < key: break
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key
```

<br>

## 비교 기반 정렬 시간의 하한
* n개 값을 정렬하는 결정트리의 각 단말노드는 가능한 정렬결과에 대응하는 하나의 순열에 해당한다
* n개 값으로부터 얻을 수 있는 순열의 수는 n!이므로, n개 값을 정렬하는 결정트리의 단말노드 개수는 n!이다
* 결정트리는 이진트리이며 높이 k인 이진트리에서 단말노드의 최대 개수는 2^k이므로 다음 식이 성립(k>=0)
  * n! < 2^k -> log2 𝑛! <= k -> 높이 k는 정수 -> ┍log2n!┒ <= k
* 따라서, 비교기반 정렬의 최악의 경우 시간복잡도의 하한은 Ω(𝑛 log 𝑛)