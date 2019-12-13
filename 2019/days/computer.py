
""""

parameter mode 0, position mode
parameter mode 1, immediate mode
parameter mode 2, relative mode

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
Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases by the value of the parameter.
Opcode 99 means that the program is finished and should immediately halt.
"""

param_count = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]


class ProgramMemory(list):
	def __getitem__(self, item):
		if item >= len(self):
			self.extend([0]*(1+item-len(self)))
		return super(ProgramMemory, self).__getitem__(item)

	def __setitem__(self, key, value):
		if key >= len(self):
			self.extend([0]*(1+key-len(self)))
		return super(ProgramMemory, self).__setitem__(key, value)


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
	program = ProgramMemory(program)
	if input_values is None:
		input_values = [0]
	i = 0
	input_i = 0
	relative_base = 0
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

		def get_parameter(p_i, pointer=False):
			p = program[i + p_i]
			if modes[p_i-1] == '1':
				assert not pointer
				return p
			if modes[p_i-1] == '2':
				p = relative_base + p
			if pointer:
				return p
			return program[p]

		if opcode is 1:  # Addition
			program[get_parameter(3, True)] = get_parameter(1) + get_parameter(2)

		elif opcode is 2:  # Multiplication
			program[get_parameter(3, True)] = get_parameter(1) * get_parameter(2)

		elif opcode is 3:  # Set
			if input_i == len(input_values):
				input_i = 0
			value = input_values[input_i]
			input_i += 1
			program[get_parameter(1, True)] = value

		elif opcode is 4:  # Get
			yield get_parameter(1)

		elif opcode is 5:  # Jump-if-true
			if get_parameter(1) != 0:
				i = get_parameter(2)
				continue

		elif opcode is 6:  # Jump-if-false
			if get_parameter(1) == 0:
				i = get_parameter(2)
				continue

		elif opcode is 7:  # Less than
			program[get_parameter(3, True)] = 1 if get_parameter(1) < get_parameter(2) else 0

		elif opcode is 8:  # Equals
			program[get_parameter(3, True)] = 1 if get_parameter(1) == get_parameter(2) else 0

		elif opcode is 9:  # Adjust Relative Base
			relative_base += get_parameter(1)

		else:
			raise ValueError("Unexpected opcode: " + str(opcode))
		i += param_count[opcode] + 1
	yield list(program)
