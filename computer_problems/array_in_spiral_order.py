
"""
Problem name: Print a given matrix in counter-clock wise spiral form

Description of the problem: Given a 2D array, print it in counter-clock wise
spiral form.

Link: https://www.geeksforgeeks.org/print-given-matrix-counter-clock-wise-spiral-form/
"""

#===========================================================
def spiral_array():

	up_ = 0
	down_ = 6
	left_ = 0
	right_ = 6

	i,j = up_, left_

	print("Array ", down_, "x", right_)
	print("\n")

	while i < down_:
		print("Inside down")
		while i < down_:
			print(i,j)
			i += 1
		i -= 1
		down_ -= 1
		print("\n")

		if j+1 < right_:
			j += 1
			print("Inside right")
			while j< right_:
				print(i,j)
				j += 1
			j -= 1
			right_ -= 1
			print("\n")

			if i-1 >= up_:
				i -= 1
				print("Inside up")
				while i>= up_:
					print(i,j)
					i -= 1
				i += 1
				up_ +=1
				print("\n")

				if j-1 > left_:
					j -= 1
					print("Inside left")
					while j > left_:
						print(i,j)
						j -= 1
					j += 1
					print("\n")

					left_ += 1
					#print("If you finish: ",up_, down_, left_, right_)
		i+=1

#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""

spiral_array()