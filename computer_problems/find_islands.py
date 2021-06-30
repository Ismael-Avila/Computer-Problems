"""

Problem name: find islands

Description of the problem: https://www.youtube.com/watch?v=4tYoVx0QoN0&t=202s

"""



#================================================================

class Node():
	def __init__(self, value = 0):
		self.value = value
		self.visited = False

#================================================================

def printer(A):
	for  i in range(len(A)):
		text = ""
		for j in range(len(A[0])):
			text = text + str(A[i][j]) + " "
		print(text)
			

#================================================================


def visited_position(row,col, A, visited_a):
	
	#This means I'm facing a 1
	if A[row][col] == 1 and visited_a[row][col].visited == False:
		#print(row, col)
		visited_a[row][col].visited = True
		visited_a[row][col].value = 1
		
		#Up
		if row-1>= 0 and A[row-1][col] == 1 and visited_a[row-1][col].visited == False :
			#print("up")
			visited_position(row-1,col,A, visited_a)

		#right
		if (col + 1 <= len(A[0])-1) and (A[row][col+1] == 1) and (visited_a[row][col+1].visited == False):
			#print("right")
			visited_position(row,col+1,A, visited_a)

		#down
		if row + 1 <= len(A)-1 and A[row+1][col] == 1 and visited_a[row+1][col].visited == False:
			#print("down")
			visited_position(row+1,col,A,visited_a)

		#left
		if col - 1 >= 0 and A[row][col-1] == 1 and visited_a[row][col-1].visited == False:
			#print("left")
			visited_position(row,col-1,A,visited_a)
		
#================================================================

def removeIslands(A):
	visited_array = [[Node() for i in range(len(A[0]))] for j in range(len(A))]
	islands = [[0 for i in range(len(A[0]))] for j in range(len(A))]
	
	up_ = 0
	down_ = len(A)

	left_ = 0
	right_ = len(A[0])

	i,j = up_, left_

	#Array in spiral order

	while i < down_:
		visited_position(i,j,A,visited_array)
		i += 1

	i -= 1

	if j+1 < right_:
		j += 1
		while j< right_:
			visited_position(i,j,A,visited_array)
			j += 1

		j -= 1

		if i-1 >= up_:
			i -= 1
			while i>= up_:
				visited_position(i,j,A,visited_array)
				i -= 1

			i += 1

			if j-1 > left_:
				j -= 1
				visited_position(i,j,A,visited_array)
				while j > left_:
					j -= 1
					visited_position(i,j,A,visited_array)
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			if A[i][j] == 1 and visited_array[i][j].visited == False:
				islands[i][j] = 1
				A[i][j] = 0

	return A,islands
				

#================================================================

"""
#================================================================#
#															Main														   #
#================================================================#
"""

"""
#Other case

A = [[1,1,0,1,0,1],
		 [0,1,0,1,0,0],
		 [1,1,0,0,1,0],
		 [0,0,0,0,1,0],
		 [1,0,1,1,0,0],
		 [1,0,0,0,0,0]]
"""

A = [[1,1,1,1,1,1],
		 [1,1,1,1,1,1],
		 [1,1,1,1,1,1],
		 [1,1,1,1,1,1],
		 [1,1,1,1,1,1],
		 [1,1,1,1,1,1]]

print("Input: ")
printer(A)
print("\n")

A, I = removeIslands(A)

print("Output: ")
printer(A)
print("------------")
printer(I)