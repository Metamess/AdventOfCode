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
	The output from amplifier E is now connected into amplifier A's input.
	The amplifiers need totally different phase settings: integers from 5 to 9
	These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting.
	Find the largest output signal that can be sent to the thrusters
	"""
	possible_settings = list(permutations(range(5, 10)))
	max_output = -99999999
	for setting in possible_settings:
		input_values = [[x] for x in setting]
		input_values[0].append(0)
		amplifiers = [computer.get_computer(read_input(), input_value) for input_value in input_values]
		next_amp_id = list(range(1,5)) + [0]
		while True:
			for amp_id in range(5):
				input_values[next_amp_id[amp_id]].append(next(amplifiers[amp_id]))
			if type(input_values[0][-1]) == list:
				value = input_values[0][-2]
				max_output = max(max_output, value)
				break
	print(max_output)


def read_input():
	with open('input/day7.txt') as input_file:
		return [int(x) for x in input_file.readline().split(',')]
