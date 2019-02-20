#！/bin/python

def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        for j in reversed(range(-1, i)):
            if tmp < arr[j]: 
                arr[j+1] = arr[j]
            else: break

        arr[j+1] = tmp

    return arr

arr = [9, 2, 14, 8, 5, 11, 4, 28, 73, 2]
arrSort = insertion_sort(arr)
print(arrSort)

