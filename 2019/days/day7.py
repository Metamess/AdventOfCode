from . import computer
from itertools import permutations


def part1():
	"""
	There are five amplifiers connected in series; each one receives an input signal and produces an output signal.
	When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier
	for its current phase setting (an integer from 0 to 4).
	Each phase setting is used exactly once, but the Elves can't remember which amplifier needs which phase setting.
	Find the largest output signal that can be sent to the thrusters by trying every possible combination of phase settings on the amplifiers.
	"""
	possible_settings = list(permutations(range(5)))
	max_output = -99999999
	for setting in possible_settings:
		value = 0
		for amp in range(5):
			program = read_input()
			output = []
			computer.run_program(program, input_values=[setting[amp], value], output_values=output)
			value = output[-1]
		max_output = max(max_output, value)
	print(max_output)


def part2():
	"""
	What is the diagnostic code for system ID 5?
	"""
	program = read_input()
	computer.run_program(program, 5)


def read_input():
	with open('input/day7.txt') as input_file:
		return [int(x) for x in input_file.readline().split(',')]
