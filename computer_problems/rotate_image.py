"""

Problem name : Rotate image

Description of the problem: You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise). You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly. DO NOT allocate another
2D matrix and do the rotation.
"""


#==========================================================

def rotate_image(A):
	N = len(A)

	#Transpose a matrix
	for i in range(N):
		for j in range(i, N):
			temp =  A[i][j]
			A[i][j] = A[j][i]
			A[j][i] = temp

	#Flip columns

	for j in range(N//2):
		for i in range(N):
			temp = A[i][j]
			A[i][j] = A[i][N-1-j]
			A[i][N-1-j] = temp

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

A = [[1,2,3], [4,5,6], [7,8,9]]
rotate_image(A)
print(A)

A = [[1,2], [3,4]]
rotate_image(A)
print(A)