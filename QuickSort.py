# CPS305 - F2020 - Lab 3
# Your Name David Tran
# Your Student Number 500890757

arr = [75, 0, 4, -12, 42, 6, 34, 62, 55, 97, 33, 16, 87, 6, 19]

def partition(arr, lower, upper):
    i = (lower-1)         # index of smaller element
    pivot = arr[upper]     # pivot
 
    for j in range(lower, upper):
        if arr[j] >= pivot:
            i = i+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1]
    arr[i+1] = arr[upper]
    arr[upper] = temp
    return (i+1)

def quickSort(arr,lower,upper):
    # Your code here
    if len(arr) == 1:
        return arr
    if lower < upper:
        p = partition(arr, lower, upper)
        quickSort(arr, lower, p-1)
        quickSort(arr, p+1, upper)

 


# You can add helper functions as well if needed

quickSort(arr,0,len(arr)-1)
print(arr)
