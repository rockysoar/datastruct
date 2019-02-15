#! /bin/python

def sort_bubble(arr):
    i, j = 0, 1
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i], arr[j] = arr[j], tmp

    return arr 

arr = [9, 2, 14, 8, 5, 11, 4, 28, 73, 2]
arrSorted = sort_bubble(arr)
print(arrSorted)

