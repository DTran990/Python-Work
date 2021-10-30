arr=[86,0,66,31,90,78,54,72,91,27,69,6,41,3,96,68,56,12]
print("Unsorted Array:", arr)


for i in range(len(arr)):
	if i+1 < len(arr):
		for j in range(i+1,len(arr)):
			if arr[i]< arr[j]:
				temp = arr[i]
				arr[i]= arr[j]
				arr[j] = temp

print("Sorted Array:",arr)
