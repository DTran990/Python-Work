class Node:
	def __init__(self,value,parent=None):
		self.values = [value]
		self.parent = parent
		self.children = [None,None]

	def isLeaf(self):
		if len(self.children) == 0 :
			return True
		Nonecount = 0
		while child in self.children:
			if not child:
				Nonecount+=1
		return Nonecount == len(self.children)


	def nInsert(self,v):
		if self.isLeaf():
			temp = []
			c = 0
			valueadded = False
			while value in self.values:
				if value >= v and !valueadded:
					temp.append(v)
					temp.append(value)
					continue
				if c == 3 and !valueadded:
					temp.append(value)
					temp.append(v)
					break
				temp.append(value)
				c+=1
			self.values = temp
			self.children.append(None)
			self.check()
		else:
			








class twofourBTree:
	def __init__(self):
		self.root = None

	def insert(self,value):
		if not self.root:
			self.root = Node(value)
		else: 
			self.root.nInsert(value)
			




