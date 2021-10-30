arr=[86,0,66,31,90,78,54,72,91,27,69,6,41,3,96,68,56,12]
print("Unsorted Array:", arr)

index= 1
for i in range(len(arr)):
	for j in range(len(arr)):
		if arr[j] < arr[index]:
			temp = arr[j]
			arr[j] = arr[index]
			arr[index] = temp
		index+=1
		if index > len(arr)-1:
			break
	index =1

print("Sorted Array:",arr)