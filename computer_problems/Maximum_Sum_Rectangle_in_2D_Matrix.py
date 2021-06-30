"""
Problem name: Maximum sum rectangle in a 2D matrix

Description of the problem: Given a 2D array, find the maximum sum
subarray in it. For example, in the following 2D array, the maximum
sum subarray is highlighted with blue rectangle and sum of this
subarray is 29.

Example:		[ 1  2 -1 -4 -20]
						[-8 -3  4  2  1]
						[ 3  8 10  1  3]
						[-4 -1  1  7 -6]


Result:			[-3  4 2]
						[ 8 10 1]
						[-1  1 7]

Space complexity O(rows)
Time complexity O((Cols+Cols-1+Cols-2 + ... + 1) x rows )

"""

"""
#Note: in this exercise we use of a helper function called "get_max_subarray"
(A function used in another similar problem) to solve in a faster way this
problem.
"""

#===========================================================

import numpy as np
from Maximum_Sum_Rectangle_in_1D_Matrix import get_max_subarray

def get_max_sum(A):
	horizontal_sumator = np.zeros(A.shape[0])

	#Horizontal coordinates
	left, right = 0,0
	
	#Vertical coordinates
	top, bottom = 0,0

	#Track our sums
	global_sum = A[0,0]

	for h_iterator in range(A.shape[1]):

		for cols in range(h_iterator,A.shape[1]):
			horizontal_sumator = horizontal_sumator+A[:,cols]

			current_sum, top_, bottom_ = get_max_subarray(horizontal_sumator)

			if current_sum > global_sum:
				left = h_iterator
				right= cols

				top = top_
				bottom =  bottom_
				global_sum =  current_sum

		horizontal_sumator = np.zeros(A.shape[0])

	return global_sum, A[top:bottom+1, left:right+1]

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

#Case 1
A = np.array([[2, 1, -3, -4, 5],
							[0, 6, 3, 4, 1],
							[2, -2, -1, 4,-5],
							[-3, 3, 1, 0, 3]], dtype='int16')

sum_, subarray = get_max_sum(A)
print("Array: \n", A)
print("Max sum: ", sum_)
print("Subarray \n", subarray)
print("\n")


#Case 2
A = np.array([[1, 2, -1, -4, -20],
							[-8, -3, 4, 2, 1],
							[3, 8, 10, 1, 3],
							[-4, -1, 1, 7, -6]], dtype='int16')

sum_, subarray = get_max_sum(A)
print("Array: \n", A)
print("Max sum: ", sum_)
print("Subarray \n", subarray)
print("\n")
