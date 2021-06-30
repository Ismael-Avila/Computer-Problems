"""

Problem name: Find the Duplicate Number

Description of the problem: Given an array of integers nums containing n + 1
integers where each integer is in the range [1, n] inclusive. There is only one
repeated number in nums, return this repeated number. You must solve the problem
without modifying the array nums and uses only constant extra space.

"""
#===========================================================

def findDuplicate(A):
	output = []

	for idx  in range(len(A)):

		if(A[abs(A[idx])-1] < 0) :
			output.append(abs(A[idx]))
			return output
		else:
			A[abs(A[idx])-1] = -1*A[abs(A[idx])-1]

	return output

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

nums = [1,3,4,2,2]

print(findDuplicate(nums))