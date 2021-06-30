#===========================================================

class list_():
	def __init__(self, value = None):
		self.value = value
		self.next = None

#===========================================================

def print_values(head):
	temp = head
	while(temp != None):
		print(temp.value)
		temp = temp.next

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

head = list_(1)
head.next = list_(2)
head.next.next = list_(3)
head.next.next.next = list_(4)
head.next.next.next.next = list_(5)
head.next.next.next.next.next = list_(6)
head.next.next.next.next.next.next = list_(7)

print_values(head)