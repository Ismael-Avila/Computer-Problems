
#===========================================================
class Node():
	def __init__(self,value = None):
		self.value = value
		self.left =  None
		self.right = None

#===========================================================

def build_max_heap_tree(A, head, index):

		head.value = A[index-1]

		left =  2*index
		right = 2*index + 1

		if left <= len(A):
			head.left = Node()
			build_max_heap_tree(A, head.left, left)
		
		if right <= len(A):
			head.right = Node()
			build_max_heap_tree(A, head.right, right)

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

head = Node()

A = [1,2,3,4,5,6,7,8]


build_max_heap_tree(A,head,1)

print(head.value)
print(head.left.value, head.right.value)
print(head.left.left.value, head.left.right.value, head.right.left.value, head.right.right.value)
print(head.left.left.left.value)
