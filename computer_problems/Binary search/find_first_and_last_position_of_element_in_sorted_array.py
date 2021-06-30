"""

Problem name: Find First and Last Position of Element in Sorted Array

Description of the problem: Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value. If target is not found
in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime
complexity

"""

#===================================================================

def find_left(A, element):
	begin = 0
	end = len(A)-1
	left = None

	while(begin<= end):
		middle_point =  begin + (end-begin)//2

		if element <= A[middle_point]:
			if element == A[middle_point]:
				left = middle_point
			end =  middle_point-1
		#element>A[middle_point]
		else:
			begin = middle_point + 1

	return left

#===================================================================

def find_right(A, element):
	begin = 0
	end = len(A)-1
	right = None

	while(begin<= end):
		middle_point =  begin + (end-begin)//2

		if element >= A[middle_point]:
			if element == A[middle_point]:
				right = middle_point
			begin = middle_point + 1
		#element < A[middle_point]:
		else:
			end =  middle_point-1
	return right

#===================================================================

def searchRange(A, element):
	output = [-1,-1]
	output[0] = find_left(A,element)
	output[1] = find_right(A, element)

	return output

#===================================================================


"""
#===================================================================#
#															Main																	#
#===================================================================#
"""


A = [5, 7, 7, 8, 8, 10]

print(searchRange(A, 10))