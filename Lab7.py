class Node:
	def __init__(self,value = None , child = None, parent = None):
		self.leftchildren = [child]
		self.rightchildren = [child]
		self.parent = parent
		self.value = [value]
class TwoFourBTree:
	def __init__(self, value):
		self.root = Node(value)
	def insert(self,value):
		