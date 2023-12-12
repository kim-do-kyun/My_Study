def insertionSort(v):
    for i in range(1, len(v)):
        key = v[i]
        j = i-1
        while j>=0:
            if v[j] < key: break
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key

v=[8,7,6,5,4,3,2,1]
insertionSort(v)
print(v)