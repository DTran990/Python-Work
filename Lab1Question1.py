from array import *
ar = array('i', [9,13,21,4,11,7,1,3])
newar = array('i',[])
arhalflength = len(ar)//2
count=0
total=0
average1 = 0
average2 = 0

for i in range(arhalflength,len(ar)):
	newar.append(ar[i])
	count+=1
	total+=ar[i]
average2 = total/count
count=0
total=0
for j in range(0,arhalflength):
	newar.append(ar[j])
	count+=1
	total+=ar[j]
average1 = total/count

print(ar)
print(newar)

print("Average for first half:",average1)
print("Average for second half:",average2)
for i in range(5,0,-1):
	print(i)