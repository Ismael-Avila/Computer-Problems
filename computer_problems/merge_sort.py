#===========================================================

def merge_sort(A):

	N = len(A)

	if N>1:
		middle_point = len(A)//2

		left_side = A[:middle_point]
		right_side = A[middle_point:]

		merge_sort(left_side)
		merge_sort(right_side)

		l = 0
		r = 0
		index = 0

		while(l<len(left_side) and r<len(right_side)):
			if (left_side[l]<right_side[r]):
				A[index] = left_side[l]
				l +=1
			else:
				A[index] = right_side[r]
				r += 1
			index += 1

		while(l<len(left_side)):
			A[index] = left_side[l]
			index += 1
			l += 1

		while(r<len(right_side)):
			A[index] = right_side[r]
			index += 1
			r += 1

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [6, 5, 4, 3, 2, 1]

print("Array: ", A)
merge_sort(A)
print("Sorted array: ",A)
print("\n")



A = [100, 2, 4, 3, 5, 1]

print("Array: ", A)
merge_sort(A)
print("Sorted array: ",A)
print("\n")
