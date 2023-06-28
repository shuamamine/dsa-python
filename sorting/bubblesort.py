def bubbleSort(a):
    l = len(a)
    for i in range(l):
        for j in range(0, l-i-1):
            if a[j] > a[j+1]:
                (a[j], a[j+1]) = (a[j+1], a[j])


a = [6, 2, 5, 7, 1, 4, 3]
bubbleSort(a)
print("The Sorted Array is:")
print(a)
