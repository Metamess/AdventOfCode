from . import computer


def part1():
	"""
	Opcode 1 adds together numbers read from two positions and stores the result in a third position.
	Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
	Opcode 99 means that the program is finished and should immediately halt.
	Before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
	What value is left at position 0 after the program halts?
	"""
	program = read_input()
	program[1] = 12
	program[2] = 2
	program = computer.run_program(program)
	print(program[0])


def part2():
	"""
	Determine what pair of inputs produces the output 19690720.
	Each of the two input values will be between 0 and 99, inclusive.
	The value placed in address 1 is called the noun, and the value placed in address 2 is called the verb.
	What is 100 * noun + verb?
	"""
	desired = 19690720
	base_program = read_input()
	for noun in range(100):
		for verb in range(100):
			program = base_program.copy()
			program[1] = noun
			program[2] = verb
			res = computer.run_program(program)[0]
			if res == desired:
				print(100 * noun + verb)
				exit()
	raise ValueError("No noun/verb combination found resulting in " + str(desired))


def read_input():
	with open('input/day2.txt') as input_file:
		return [int(x) for x in input_file.readline().split(',')]


