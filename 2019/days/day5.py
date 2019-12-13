from . import computer


def part1():
	"""
	After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?
	"""
	program = read_input()
	computer.run_program(program, [1])


def part2():
	"""
	What is the diagnostic code for system ID 5?
	"""
	program = read_input()
	computer.run_program(program, [5])


def read_input():
	with open('input/day5.txt') as input_file:
		return [int(x) for x in input_file.readline().split(',')]
