"""
Problem name: Decode string

Description of the problem: Given an encoded string, return its decoded string. The
encoding rule is: k[encoded_string], where the encoded_string inside the square brackets i
being repeated exactly k times. Note that k is guaranteed to be a positive integer. You
may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k. For example, there won't be input
like 3a or 2[4].
"""

#===========================================================

def decodeString(S):
	strings = []
	counters = []
	current_string = ""
	idx = 0

	while idx <len(S):

		char =  S[idx]

		if char.isdigit():
			count = 0

			while char.isdigit():
				count = 10*count + int(char) 
				idx += 1
			counters.append(count)
		elif char == "[":
			strings.append(string)
			string = ""
			idx += 1

		elif char == "]":
			temp = string.pop()

			for i in range(counters.pop()):
				temp = temp + string
			string =  temp
			idx += 1

		#If char is alpha
		else:
			string = string + char
			idx += 1
			
	return string_

#===========================================================

"""
#===========================================================#
#														Main														#
#===========================================================#
"""

a = "3[a]2[bc]"

print(decodeString(a))