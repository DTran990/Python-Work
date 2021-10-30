from array import *

arr= array('i',[1,4,14,2,1,3,5,6,23])
newarr = array('i',[])
oddarr =array('i',[])

for ele in arr:
	if ele%2==0:
		newarr.append(ele)
	else:
		oddarr.append(ele)

for odd in oddarr:
	newarr.append(odd)

print(newarr)