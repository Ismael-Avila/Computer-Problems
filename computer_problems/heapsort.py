#===========================================================

def heapsort(A):
	n = len(A)
	build_max_heap(A)

	for i in reversed(range(1,n+1)):
		temp = A[0]
		A[0] = A[i-1]
		A[i-1] = temp
		heapify(A,1,i-1)


#===========================================================

def build_max_heap(A):
	n = len(A)//2
	N = len(A)
	for i in reversed(range(1,n+1)):
		heapify(A, i,N)



#===========================================================

def heapify(A, node,n):
	left_node = 2*node
	right_node = 2*node + 1

	if left_node <= n and A[left_node-1] > A[node-1]:
		max_ = left_node
	else:
		max_ = node

	if right_node <= n and A[right_node-1] >A[max_-1]:
		max_ = right_node

	if max_!=node:
		temp = A[node-1]
		A[node-1] = A[max_-1]
		A[max_-1] = temp
		heapify(A, max_,n)

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [1,2,3,4,5,6,7,8]

print(A)
print("\n")
heapsort(A)
print(A)