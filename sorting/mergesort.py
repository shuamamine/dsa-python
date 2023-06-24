def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        arr1 = a[:mid]
        arr2 = a[mid:]

        mergeSort(arr1)
        mergeSort(arr2)

        i = j = k = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ar[k] = arr1[i]
                i += 1
            else:
                ar[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            ar[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            ar[k] = arr2[j]
            j += 1
            k += 1


arr = [6, 2, 5, 7, 1, 4, 3]
mergeSort(arr)
print("Sorted Array is:")
print(arr)
