
def part1():
	"""
	The password:
	- It is a six-digit number.
	- The value is within the range given in your puzzle input.
	- Two adjacent digits are the same (like 22 in 122345).
	- Going from left to right, the digits never decrease; they only ever increase or stay the same.
	How many different passwords within the range given in your puzzle input meet these criteria?
	"""
	[min_value, max_value] = read_input()

	# start = ''
	# prev = 0
	# for d in min_value:
	# 	if int(d) < prev:
	# 		start += prev * (6 - len(start))
	# 		break
	# 	prev = int(d)
	# 	start += d

	def is_valid(number):
		prev = -1
		has_double = False
		for d in str(number):
			if int(d) < prev:
				return False
			if int(d) == prev:
				has_double = True
			prev = int(d)
		return has_double

	count = 0
	for i in range(int(min_value), int(max_value)):
		if is_valid(i):
			count += 1
	print(count)


def part2():
	"""
	The two adjacent matching digits are not part of a larger group of matching digits.
	How many different passwords within the range given in your puzzle input meet all of the criteria?
	"""
	[min_value, max_value] = read_input()

	def is_valid(number):
		prev = -1
		has_double = False
		streak = 0
		for d in str(number):
			if int(d) < prev:
				return False
			if int(d) == prev:
				streak += 1
			else:
				if streak == 1:
					has_double = True
				streak = 0
			prev = int(d)
		if streak == 1:
			has_double = True
		return has_double

	count = 0
	# for i in range(int(min_value), int(max_value)):
	for i in range(int(min_value), int(max_value)):
		if is_valid(i):
			count += 1
	print(count)


def read_input():
	with open('input/day4.txt') as input_file:
		return input_file.readline().split('-')
