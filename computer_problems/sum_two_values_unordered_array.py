"""
Problem name: Two Sum

Description of the problem:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. You may assume that each input would have
exactly one solution, and you may not use the same element twice. You can return
the answer in any order.

"""

#===========================================================

def sum_values(A, value):
	hash_ = dict()
	result = [0,0]

	
	for idx in range( len(A)):
		current_value =  A[idx]

		if current_value in hash_.keys():
			result[0] = hash_[current_value]
			result[1] = idx
			return result
		else:
			hash_[value -  current_value] =  idx

	print(hash_)
	return "No result found"

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

value = 11
A= [2,1,7,3,11,0]

print("Current array: ")
print(A)
print("Value to be sumed up")
print(value)
print("\n")
print("Result")
print(sum_values(A,value))