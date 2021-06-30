#===================================================================

def preorder(head):
	
	if head != None:
		print(head.value)
		preorder(head.left)
		preorder(head.right)

#===================================================================

class Node():
	def __init__(self, value):
		self.value =  value
		self.left =  None
		self.right = None

#===================================================================


"""
#===================================================================#
#															Main																	#
#===================================================================#
"""

head = Node(1)

head.left = Node(2)
head.right = Node(3)

head.left.left = Node(4)
head.left.right = Node(5)

head.right.left = Node(6)
head.right.right = Node(7)

head.left.left.left = Node(8)


print(head.value)
print(head.left.value, head.right.value)
print(head.left.left.value, head.left.right.value, head.right.left.value, head.right.right.value)
print(head.left.left.left.value)

print("\n----------------------------")
print("\n")
preorder(head)

