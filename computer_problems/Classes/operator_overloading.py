"""
Operator overloading: Modifying the way of how an operator interacts with two
types of objects.
"""

#===========================================================

class student():

	def __init__(self, value_1, value_2):
		self.value_1 = value_1
		self.value_2 = value_2

	def printer(self):
		print("Value 1: ", self.value_1)
		print("Value 2: ", self.value_2)

	def __add__(self, other):
		m1 = self.value_1 + other.value_1
		m2 = self.value_2 + other.value_2
		st3 = student(m1,m2)
		return st3

	def __gt__(self, other):
		v1 = self.value_1 + self.value_2
		v2 = other.value_1 + other.value_2

		if v1 > v2:
			return True
		else:
			return False

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

#Setting some students
st1 = student(2,3)
st2 = student(3,1)


#Applying operator overloading
print("Operator overloading with +:")
st3 = st1 + st2
st3.printer()
print("\n")

print("Operator overloading with >:")
if st1>st2:
	print("st1 is grather than st2")
else:
	print("st2 is grather than st1")