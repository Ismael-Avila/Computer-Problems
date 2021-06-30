"""
Problem name: Find All Duplicates in an Array

Description of the problem: Given an integer array nums of length n where all
the integers of nums are in the range [1, n] and each integer appears once or
twice, return an array of all the integers that appears twice. You must write
an algorithm that runs in O(n) time and uses only constant extra space.

"""
#===========================================================

def findDuplicates(A):
	output = []
	for idx in range(len(A)):
		if A[abs(A[idx])-1] < 0:
			output.append(abs(A[idx]))
		else:
			A[abs(A[idx])-1] = -A[abs(A[idx])-1]
	return output

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [4,3,2,7,8,2,3,1,4]

print(findDuplicates(A))