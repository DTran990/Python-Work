class Node: #Node Class to create new node objects containing two children. Also Saves height
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		self.height = 1
class AVL:
	def getheight(self,root): # Returns height of the root
		if not root:
			return 0
		return root.height

	def leftRotation(self,root): #Performs a left rotation rebalance
		newroot = root.right # shifts right child to the position of the root of a new node
		temp = newroot.left
		newroot.left = root #shifts original root to left child
		root.right = temp #shifts the left child of original root to the right child of the new root
		if self.getheight(root.left) > self.getheight(root.right): # if statements to calculate for the height for the root
			root.height = 1 + self.getheight(root.left)
		elif self.getheight(root.left) < self.getheight(root.right):
			root.height = 1 + self.getheight(root.right)
		else: 
			root.height = 1 +self.getheight(root.right)
		if self.getheight(newroot.left) > self.getheight(newroot.right): # if statements to calculate for the height for the rebalanced root
			newroot.height = 1 + self.getheight(newroot.left)
		elif self.getheight(newroot.left) < self.getheight(newroot.right):
			newroot.height = 1 + self.getheight(newroot.right)
		else: 
			newroot.height = 1 +self.getheight(newroot.right)
		return newroot

	def rightRotation(self,root):
		newroot = root.left #shifts the left child to the root of a new node
		temp = newroot.right
		newroot.right = root #shifts the original root to the right child of the new root
		root.left = temp #moves the right child of the right child of the original root to the left child of the new root

		if self.getheight(root.left) > self.getheight(root.right): # if statements to calculate for the height for the root
			root.height = 1 + self.getheight(root.left)
		elif self.getheight(root.left) < self.getheight(root.right):
			root.height = 1 + self.getheight(root.right)
		else: 
			root.height = 1 +self.getheight(root.right)
		if self.getheight(newroot.left) > self.getheight(newroot.right): # if statements to calculate for the height for the new root
			newroot.height = 1 + self.getheight(newroot.left)
		elif self.getheight(newroot.left) < self.getheight(newroot.right):
			newroot.height = 1 + self.getheight(newroot.right)
		else: 
			newroot.height = 1 +self.getheight(newroot.right)
		return newroot

	def getMinValue(self,root): #returns the smallest value
		if root == None or root.left == None:
			return root
		return self.getMinValue(root.left)


	def insert(self, root, value):

		if not root:
			return Node(value)
		elif value < root.value: #if the value is smaller than the current node, go down the left of the tree
			root.left = self.insert(root.left,value)
		else: # if the value is larger than the current node, go down the right of the tree
			root.right = self.insert(root.right,value)

		if self.getheight(root.left) > self.getheight(root.right):  # if statements to calculate for the height for the root
			root.height = 1 + self.getheight(root.left)
		elif self.getheight(root.left) < self.getheight(root.right):
			root.height = 1 + self.getheight(root.right)
		else: 
			root.height = 1 +self.getheight(root.right)
		balance = 0 if not root else self.getheight(root.left) - self.getheight(root.right)  # calculates the balance for the current node

		if balance > 1 and value < root.left.value: #right-right case
			return self.rightRotation(root)
		if balance < -1 and value > root.right.value: #left-left case
			return self.leftRotation(root)
		if balance > 1 and value > root.left.value: #left-right case
			root.left = self.leftRotation(root.left)
			return self.rightRotation(root)
		if balance < -1 and value < root.right.value: #right-left case
			root.right = self.rightRotation(root.right)
			return self.leftRotation(root)
		return root
	def delete(self,root,value):

		if not root:
			return root
		elif value < root.value: #if the value is smaller than the current node, go down the left of the tree
			root.left = self.delete(root.left,value)
		elif value > root.value: #if the value is larger than the current node, go down the right of the tree
			root.right = self.delete(root.right,value)
		else: #if value is equal to the current node value, then delete the node and set its child as the child of the parent.
			if root.left == None:
				temp = root.right
				root = None
				return temp
			elif root.right == None:
				temp = root.left 
				root = None
				return temp
			temp = self.getMinValue(root.right)
			root.value = temp.value
			root.right = self.delete(root.right,temp.value)
		if root == None:
			return root

		if self.getheight(root.left) > self.getheight(root.right): #if statement to calculate the node height
			root.height = 1 + self.getheight(root.left)
		elif self.getheight(root.left) < self.getheight(root.right):
			root.height = 1 + self.getheight(root.right)
		else: 
			root.height = 1 +self.getheight(root.right)
		balance = 0 if not root else self.getheight(root.left) - self.getheight(root.right) #calculate the balance value of the node
		balanceleft = 0 if not root.left else self.getheight(root.left.left) - self.getheight(root.left.right)  #calculate the balance of the left child
		balanceright = 0 if not root.right else self.getheight(root.right.left) - self.getheight(root.right.right)  #calculate the balance of the right child


		if balance > 1 and balanceleft >=0: #right-right case
			return self.rightRotation(root)
		if balance < -1 and balanceright <= 0 : #left-left case
			return self.leftRotation(root)
		if balance > 1 and balanceleft < 0: #left-right case
			root.left = self.leftRotation(root.left)
			return self.rightRotation(root)
		if balance < -1 and balanceright > 0: #right-left case
			root.right = self.rightRotation(root.right)
			return self.leftRotation(root)
		return root

	def inOrder(self,root): #prints out the tree in inOrder format
		if not root:
			return 
		self.inOrder(root.left)
		print(root.value," ", end = "")
		self.inOrder(root.right)


Tree = AVL() 
root = None
root = Tree.insert(root,23)
root = Tree.insert(root,5)
root = Tree.insert(root,43)
root = Tree.insert(root,0)
root = Tree.insert(root,12)
root = Tree.insert(root,26)
root = Tree.insert(root,99)
root = Tree.insert(root,1)
root = Tree.insert(root,2)

 
Tree.inOrder(root) 
print()

  
 
value = 26
root = Tree.delete(root, value) 
  
 
Tree.inOrder(root) 
print()
