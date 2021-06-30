#===========================================================

def heapsort(A):

	N = len(A)
	build_max_heap(A)
	
	for n in reversed(range(1,N+1)):
		temp =  A[0]
		A[0] =  A[n-1]
		A[n-1] = temp

		Heapify(A,1,n-1)
	



#===========================================================
def build_max_heap(A):
	n = len(A)//2
	N = len(A)

	for i in reversed(range(1,n+1)):
		Heapify(A, i,N)



#===========================================================
def Heapify(A, i,n):
	left = 2*i
	right = 2*i+1

	if left <= n and A[left-1].final_grade > A[i-1].final_grade:
		max_ = left
	else:
		max_ = i

	if right <= n and A[right-1].final_grade > A[max_-1].final_grade:
		max_ = right

	if max_ != i:
		temp = A[i-1]
		A[i-1] = A[max_-1]
		A[max_-1] = temp
		Heapify(A,max_,n)


#===========================================================

class student():
	def __init__(self, name, last_name):
		self.name= name
		self.last_name = last_name
		self.grades = None
		self.final_grade = None

	def set_grades(self,grades):
		self.grades = grades

	def average_grade(self):
		if self.grades  != None:
			sum_ = 0
			for i in range(len(self.grades)):
				sum_ = sum_ + self.grades[i]

			self.final_grade = sum_/len(self.grades)
		else:
			print("The current grades are empty!!!")


#===========================================================


"""
#===========================================================#
#														Main														#
#===========================================================#
"""


#Setting some students

st1 = student("Luis", "Miguel")
st1.set_grades([8,9,7,10,7])
st1.average_grade()

st2 = student("Marco", "Antonio")
st2.set_grades([8,7,7,7,7])
st2.average_grade()

st3 = student("Michael", "Klein")
st3.set_grades([9,9,7,10,9])
st3.average_grade()



#Create a list of students
students = []

students.append(st1)
students.append(st2)
students.append(st3)



#We sort the students acording their notes with heapsort
heapsort(students)
for s in range(len(students)):
	print(students[s].name, " ", students[s].last_name, " Final grade:",  students[s].final_grade)
print("\n")
