# YOUR NAME David Tran  
# YOUR STUDENT NUMBER 50089757

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
    def __str__(self):
        node = self.headval
        output = "[ "
        while(node != None):
            output = output + str(node.dataval) + ", "
            node = node.nextval
        if(len(output) > 2):
            output = output[:-2]
        return output + " ]"

# DO NOT EDIT ANY CODE ABOVE THIS LINE
    def insert(self, val):
        # Fill in this method, which takes a value and adds a node which holds the value at the end of the linked list
        new = Node(val)
        if self.headval == None:
                self.headval = new
                return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = new
        

    def delete(self, index=0):
        # Fill in this method, which takes an index(with a default value of 0), and deletes the node at the index specified
        if self.headval == None: 
            return
        temp = self.headval
        if index == 0:
            self.headval=temp.nextval
            temp = None
            return
        for i in range(index-1):
            temp = temp.nextval
            if temp == None:
                break
            if temp == None:
                return
            if temp.nextval == None:
                return
            nextval = temp.nextval.nextval
            temp.nextval = None
            temp.nextval=nextval



    def find(self, val):
        # Fill in this method, which takes in a value and returns the index of the first node which contains that value. If no node containing that value is found, return False
        current = self.headval
        count = 0
        while current != None:
            if current.dataval == val:
                return count
            current = current.nextval
            count+=1
        return False
    def reverse(self):
        # Fill in this method, which reverses the list
        prev = None
        current = self.headval
        while (current != None):
            nextval = current.nextval
            current.nextval = prev
            prev = current
            current = nextval
        self.headval = prev
#DO NOT EDIT ANY CODE PAST THIS LINE

# Tests
# Insertion
a = LinkedList()
a.insert(1)
a.insert(2)
a.insert('a')
a.insert(3)
print(str(a) == "[ 1, 2, a, 3 ]")

# Deletion
a.delete()
print(str(a) == "[ 2, a, 3 ]")
a.delete(2)
print(str(a) == "[ 2, a ]")

# Find
a.insert('b')
a.insert('c')
a.insert('b')
print(a.find('b') == 2)
print(a.find('c') == 3)
print(a.find('d') == False)

# Reverse
a.reverse()
print(str(a) == "[ b, c, b, a, 2 ]")

