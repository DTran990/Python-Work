# CPS305 - F2020 - Lab 3
# Your Name David Tran	
# Your Student Number 500890757

arr = [75, 0, 4, -12, 42, 6, 34, 62, 55, 97, 33, 16, 87, 6, 19]
def heapify(arr, n, i): 
    smallest = i 
    l = 2 * i + 1      
    r = 2 * i + 2    
  

    if l < n and arr[i] > arr[l]: 
        smallest = l 
  

    if r < n and arr[smallest] > arr[r]: 
        smallest = r 

    if smallest != i: 
        arr[i],arr[smallest] = arr[smallest],arr[i]  
        heapify(arr, n, smallest)
def heapSort(arr):
    # Your code here
    n = len(arr) 
   
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 
# You can add helper functions as well if needed

heapSort(arr)
print(arr)