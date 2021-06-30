"""
Problem name: Squares of a Sorted Array

Description of the problem: Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

"""

#===========================================================

def sortedSquares(A):
	left = 0
	right = len(A)-1
	output = [0]*len(A)
	counter = len(A)-1

	while(left<=right):
		if abs(A[left])<abs(A[right]):
			output[counter] = A[right] * A[right]
			right -= 1
		else:
			output[counter] = A[left] * A[left]
			left += 1

		counter -= 1

	return output

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

nums =  [-7,-3,2,3,11]

print("Input: ", nums)

print("Output: ", sortedSquares(nums))