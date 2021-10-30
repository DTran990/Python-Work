import sys

data =[]
new =None
for k in range(100):
	a =len(data)
	b=sys.getsizeof(data)
	if new==None:
		new=b
		print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
	elif b!=new:
		new=b
		print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
	data.append(None)

