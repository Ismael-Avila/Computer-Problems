"""
Problem name: Largest Sum Contiguous Subarray


Description of the problem:
Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers that has the largest sum.


Example:
	Array: 		[-2, -3, 4, -1, -2, 1, 5, -3]
	Indexes:	[0,  1,  2,  3,  4, 5, 6,  7]

Result:
	Sum:		4 + (-1) + (-2) + 1 + 5 = 7

	Maximum Contiguous Array Sum is 7

Space complexity: O(len(A))
Time complexity: O(len(A))
"""

#===========================================================

import numpy as np

def get_max_subarray(A):

	if A.shape[0]==0:
		return None,None,None

	elif A.shape[0]==1:
		return A[0], 0,0

	else:
		current_sum = A[0]
		global_sum = A[0]
		left= 0
		right=0


		for i in range(1,A.shape[0]):
			current_sum = current_sum + A[i]

			if current_sum<=A[i]:
				current_sum = A[i]

				if A[i]>global_sum:
					global_sum = A[i]
					left= i
					right = i
			else:
				if current_sum>global_sum:
					global_sum = current_sum
					right = i


	return global_sum, left, right

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

#Case 1
A = np.array([-2, -3, 4, -1, -2, 1, 5, -3], dtype='int16')
sum_, left, right = get_max_subarray(A)
print("Array: ", A)
print("Max sum:", sum_)
print("Subarray: ", A[left:right+1])
print("\n")


#Case 2
A = np.array([-2, 1, -3, 4, -1, 2, 1, -5, 4], dtype='int16')
sum_, left, right = get_max_subarray(A)
print("Array: ", A)
print("Max sum:", sum_)
print("Subarray: ", A[left:right+1])
print("\n")


#Case 3
A = np.array([-2], dtype='int16')
sum_, left, right = get_max_subarray(A)
print("Array: ", A)
print("Max sum:", sum_)
print("Subarray: ", A[left:right+1])
print("\n")


#Case 4
A = np.array([1,6,-2,3], dtype='int16')
sum_, left, right = get_max_subarray(A)
print("Array: ", A)
print("Max sum:", sum_)
print("Subarray: ", A[left:right+1])