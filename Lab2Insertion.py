arr=[54,26,93,17,77,31,44,55,20]
print("Unsorted Array:", arr)

for i in range(1,len(arr)):
	for j in range(i,-1,-1):
		if j -1 >= 0:
			if arr[j] < arr[j-1]:
				current= arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = current
	print(arr)



print("Sorted Array:", arr)
		 