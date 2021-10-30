import ctypes

class DynamicArray:

	def __init__(self):
		self._n=0
		self._capacity = 1
		self._A=self._make_array(self._capacity)

	def __len__(self):
		return self._n

	def __getitem__(self,k):
		if (not 0<= k < self._n) and (not self._n + k >=0):
			raise IndexError('invalid index') 
		if self._n + k >= 0 and k<0:
			return self._A[self._n + k]
		return self._A[k]

	def append(self,obj):
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		self._A[self._n] = obj
		self._n += 1

	def _resize(self,c):
		B= self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B 
		self._capacity = c

	def _make_array(self, c):
		return (c* ctypes.py_object)()

	def insert(self, k, value):
		if self._n == self._capacity:
			B= self._make_array(2*self._capacity)
			index= self._n
			for i in range(self._n,-1,-1):
				if i == k:
					B[i]=value
				else: 
					B[i] = self._A[index-1]
					index-=1
			self._A = B
		else:
			for j in range(self._n,k,-1):
				self.A[j] = self._A[j-1]
			self._A[k] = value
		self._n += 1


array = DynamicArray()
array.append(0)
array.append(1)
array.append(2)
array.append(3)

array.insert(1,5)

for i in range(array.__len__()):
	print(array.__getitem__(i))