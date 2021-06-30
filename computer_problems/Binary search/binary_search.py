#===================================================================

def binary_search(A, element):
	begin = 0
	end = len(A)-1

	while(begin <= end):

		middle_point = begin + (end-begin)//2
		
		if element == A[middle_point]:
			return middle_point
		elif element>A[middle_point]:
			begin = middle_point + 1
		else:
			end = middle_point-1


	return None

#===================================================================


"""
#===================================================================#
#															Main																	#
#===================================================================#
"""


A = [1,2,3,7,8,9]

print(binary_search(A,9))