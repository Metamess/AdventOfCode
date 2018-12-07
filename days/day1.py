
def part1():
	""""
	A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.
	Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?
	"""
	frequency = 0
	with open("input/day1.txt") as change_list:
		for change in change_list:
			frequency += int(change)
	print(frequency)


def part2():
	""""
	What is the first frequency your device reaches twice?
	"""
	frequency = 0
	visited_frequencies = {frequency}
	while True:
		with open("input/day1.txt") as change_list:
			for change in change_list:
				frequency += int(change)
				if frequency in visited_frequencies:
					print(frequency)
					return
				visited_frequencies.add(frequency)
