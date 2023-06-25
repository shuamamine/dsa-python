def insertionSort(a):
    l = len(a)
    for i in range(1, l):
        k = a[i]
        j = i-1
        while j >= 0 and k < arr[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k


a = [6, 2, 5, 7, 1, 4, 3]
insertionSort(a)
print("Sorted Array is:")
print(a)
