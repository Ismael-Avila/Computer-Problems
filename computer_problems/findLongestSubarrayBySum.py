"""
Problem name: findLongestSubarrayBySum

Description of the problem: Given an array nums and a target value k,
find the maximum length of a subarray that sums to k. If there isn't one,
return 0 instead

"""


#===========================================================

def findLongestSubarrayBySum(value, A):
	result = [0,0]
	sum_ = 0

	r = 0
	l = 0


	while(r<len(A)):
		sum_ = sum_ + A[r]

		if sum_ == value and r-l > result[1]-result[0]:
			result[1] = r
			result[0] = l

		while(sum_>value and l<r):
			sum_ = sum_ - A[l]
			l += 1

		r += 1

	return result

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [1,2,3,4,5,0,0,0, 6,7,8,9,10]

result = findLongestSubarrayBySum(15, A)

print(result)