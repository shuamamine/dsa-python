def selectionSort(a):
    l = len(a)
    for i in range(l-1):
        small = i
        for j in range(i + 1, l):
            if a[j] < a[small]:
                small = j
        (a[i], a[smallest]) = (a[smallest], a[i])


a = [6, 2, 5, 7, 1, 4, 3]
selectionSort(a)
print("Sorted Array is:")
print(a)
