
"""
Problem name: find a pair that sum up x value

Description fo the problem: Given a sorted array and a number x, find a pair in array
whose sum is x or return None if doesn't exist that pair.
"""

#===========================================================

def sum_values(A, value):
	sum_ = 0
	l = 0
	r = len(A)-1
	while(l<r and sum_ != value):
		sum_ = A[l] + A[r]

		if sum_>value:
			r -= 1

		elif sum_< value:
			l += 1
		else:
			break
	
	if sum_ == value:
		return l,r
	else:
		return None

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""


value = 100
A= [1,2,3,9,13]
print(sum_values(A,value))