#===================================================================

class sumator():

	def sum_(self, A=None, B= None, C=None):
		result = 0
		for e in [A, B, C]:
			if e != None:
				result += e
		return result

#===================================================================

"""
#===================================================================#
#															Main																	#
#===================================================================#
"""


object_ = sumator()
sum_1 = object_.sum_(1,2)
sum_2 = object_.sum_(1,2,3)

print(sum_1)
print(sum_2)