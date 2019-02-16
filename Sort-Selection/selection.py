#! /bin/python

def sort_selection(arr):
    for i in range(0, len(arr)-1):
        min_ = i
	for j in range(i+1, len(arr)):
	    if arr[j] < arr[min_]: min_ = j

	if min_ != i:
	    minTmp = arr[i]
	    arr[i], arr[min_] = arr[min_], minTmp
    
    return arr


arr = [9, 2, 14, 8, 5, 11, 4, 28, 73, 2]
arrSorted = sort_selection(arr)
print(arrSorted)

