
""""
Opcode 1 adds together numbers read from two positions and stores the result in a third position.
Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
Opcode 99 means that the program is finished and should immediately halt.
"""


def run_program(program):
	i = 0
	while True:
		opcode = program[i]
		if opcode is 99:
			break
		p1 = program[i + 1]
		p2 = program[i + 2]
		p3 = program[i + 3]

		if opcode is 1:
			program[p3] = program[p1] + program[p2]
		elif opcode is 2:
			program[p3] = program[p1] * program[p2]
		else:
			raise ValueError("Unexpected opcode: " + str(opcode))
		i += 4
	return program
