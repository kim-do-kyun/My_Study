def selectionSort(v):
    for i in range(len(v)):     #len(v)-1
        minIndex = i
        for j in range(i+1, len(v)):
            if v[j] < v[minIndex]:
                minIndex = j
        v[i], v[minIndex] = v[minIndex], v[i]

v = [5,4,3,2,1]
selectionSort(v)
print(v)