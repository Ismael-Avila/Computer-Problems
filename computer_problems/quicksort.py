#===========================================================

def quicksort(A):

	if len(A)<=1:
		return A

	else:

		pivot =  A.pop()

		less = []
		greater = []

		for e in A:
			if e>pivot:
				greater.append(e)
			else:
				less.append(e)

		return quicksort(less) + [pivot] + quicksort(greater)

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [6, 5, 3, 4, 2, 1]
result = quicksort(A)
print(result)

