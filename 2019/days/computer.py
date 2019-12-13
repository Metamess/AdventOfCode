
""""

parameter mode 0, position mode
parameter mode 1, immediate mode

Parameter modes are stored in the same value as the instruction's opcode.
The opcode is the rightmost two digits of the first value in an instruction.
Parameter modes are single digits, one per parameter, read right-to-left from the opcode.

Opcode 1 adds together numbers read from two positions and stores the result in a third position.
Opcode 2 multiplies together numbers read from two positions and stores the result in a third position.
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 99 means that the program is finished and should immediately halt.
"""

param_count = [0, 3, 3, 1, 1, 2, 2, 3, 3]


def run_program(program, input_values=None, output_values=None):
	if input_values is None:
		input_values = [0]
	if output_values is None:
		output_values = []
	computer_generator = get_computer(program, input_values)
	while True:
		value = next(computer_generator)
		if type(value) == list:
			return value
		output_values.append(value)


def get_computer(program, input_values=None):
	if input_values is None:
		input_values = [0]
	i = 0
	input_i = 0
	while True:
		instruction = str(program[i])
		# print('instruction: ' + instruction, i)
		if len(instruction) == 1:
			opcode = program[i]
			modes = '0' * param_count[opcode]
		else:
			opcode = int(str(instruction)[-2:])
			if opcode is 99:
				break
			# print(opcode)
			modes = str(instruction)[:-2]
			modes = modes[::-1] + '0' * (param_count[opcode] - len(modes))
		if opcode is 99:
			break

		if opcode is 1:  # Addition
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			p3 = program[i + 3]
			if modes[2] == '1':
				raise ValueError()

			program[p3] = p1 + p2

		elif opcode is 2:  # Multiplication
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			p3 = program[i + 3]
			if modes[2] == '1':
				raise ValueError()
			program[p3] = p1 * p2

		elif opcode is 3:  # Set
			p1 = program[i + 1]
			if modes[0] == '1':
				raise ValueError()
			if input_i == len(input_values):
				input_i = 0
			value = input_values[input_i]
			input_i += 1
			program[p1] = value

		elif opcode is 4:  # Get
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]
			yield p1

		elif opcode is 5:  # Jump-if-true
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			if p1 != 0:
				i = p2
				continue

		elif opcode is 6:  # Jump-if-false
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			if p1 == 0:
				i = p2
				continue

		elif opcode is 7:  # Less than
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			p3 = program[i + 3]
			if modes[2] == '1':
				raise ValueError()

			if p1 < p2:
				program[p3] = 1
			else:
				program[p3] = 0

		elif opcode is 8:  # Equals
			p1 = program[i + 1]
			if modes[0] == '0':
				p1 = program[p1]

			p2 = program[i + 2]
			if modes[1] == '0':
				p2 = program[p2]

			p3 = program[i + 3]
			if modes[2] == '1':
				raise ValueError()

			if p1 == p2:
				program[p3] = 1
			else:
				program[p3] = 0
		else:
			raise ValueError("Unexpected opcode: " + str(opcode))
		i += param_count[opcode] + 1
	yield program
