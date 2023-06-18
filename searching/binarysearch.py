# write a program for binary search

def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 2, 3, 4, 5]
key = 4
idx = binarySearch(arr, key)
if idx == -1:
    print("Item Not Found")
else:
    print(str(key), "is found at index :", str(idx))

# OUTPUT
# 4 is found at index : 3
