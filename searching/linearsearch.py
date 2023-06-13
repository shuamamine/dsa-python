# Write a program for linear search

def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [3, 9, 2, 5, 4]
k = 5 #key
index = linearSearch(arr, k)
if index == -1:
    print("Item Not Found")
else:
     print(str(k), "found at index:", str(index))
