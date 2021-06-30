#===========================================================
#Base class
class employee():
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name
		self.salary = None

	def calculate_salary(self,salary_per_day):
		self.salary = salary_per_day*30

#===========================================================
#Class that inheritences from employee
class programmer(employee):
	def __init__(self, name, last_name, experience, salary_per_day):
		super().__init__(name, last_name)
		self.experience = experience
		self.salary_per_day = salary_per_day

	def salary_complete(self):
		super().calculate_salary(self.salary_per_day)
#===========================================================
#Class that inheritences from employee
class lawyer(employee):
	def __init__(self, name, last_name, number_of_cases_solved, salary_per_day):
		super().__init__(name, last_name)
		self.number_of_cases_solved = number_of_cases_solved
		self.salary_per_day = salary_per_day

	def salary_complete(self):
		super().calculate_salary(self.salary_per_day)

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

#Setting some classes
programmer = programmer("Luis", "Michael", "Jr.", 100)
programmer.salary_complete()

lawyer = lawyer("Sabrina", "Mile", 35, 150)
lawyer.salary_complete()
