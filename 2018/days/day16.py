import json


def part1():
	"""
	Ignoring the opcode numbers, how many samples in your puzzle input behave like three or more opcodes?
	"""
	res = 0
	opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
	samples = read_input()[0]
	for sample in samples:
		correct = 0
		for opcode in opcodes:
			state = sample['before'].copy()
			opcode(sample['instruction'][1], sample['instruction'][2], sample['instruction'][3], state)
			if state == sample['after']:
				correct += 1
		if correct > 2:
			res += 1
	print(res)


def part2():
	"""
	Using the samples you collected, work out the number of each opcode and execute the test program.
	What value is contained in register 0 after executing the test program?
	"""
	# Step 1: run all samples as every opcode
	opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
	can_opcode_match_instruction = [[True for _ in range(len(opcodes))] for _ in range(len(opcodes))]
	samples, program = read_input()
	for sample in samples:
		instruction = sample['instruction']
		for opcode_index in range(len(opcodes)):
			if can_opcode_match_instruction[opcode_index][instruction[0]]:
				state = sample['before'].copy()
				# Run the opcode
				opcodes[opcode_index](instruction[1], instruction[2], instruction[3], state)
				can_opcode_match_instruction[opcode_index][instruction[0]] = (state == sample['after'])

	# Step 2: Reduce options to 1 for each opcode
	total_matches = sum([matches.count(True) for matches in can_opcode_match_instruction])
	number_to_opcode = dict()
	while total_matches > 0:
		# Find an opcode with only 1 option left
		found_index = -1
		for i, matches in enumerate(can_opcode_match_instruction):
			if matches.count(True) is 1:
				found_index = i
				break
		assert found_index != -1
		# Set this instruction option to False for all other opcodes
		instruction_number = can_opcode_match_instruction[found_index].index(True)
		number_to_opcode[instruction_number] = opcodes[found_index]
		for matches in can_opcode_match_instruction:
			matches[instruction_number] = False
		# Recalculate total_matches se we converge
		total_matches = sum([matches.count(True) for matches in can_opcode_match_instruction])

	# Step 3: Run the test program
	state = [0]*4
	for instruction in program:
		number_to_opcode[instruction[0]](instruction[1], instruction[2], instruction[3], state)
	print(state[0])


def read_input():
	samples = []
	test_program = []
	with open('input/day16.txt') as input_file:
		line = input_file.readline().rstrip('\n')
		while line:
			# Get the before state
			sample = dict()
			sample['before'] = json.loads(line[8:])
			# Get the instruction
			line = input_file.readline().rstrip('\n')
			sample['instruction'] = [int(n) for n in line.split(' ')]
			# Get the after state
			line = input_file.readline().rstrip('\n')
			sample['after'] = json.loads(line[8:])
			# skip the separating newline
			line = input_file.readline()
			samples.append(sample)
			line = input_file.readline().rstrip('\n')
		# End of samples, start of test program
		# Skip the newlines
		line = input_file.readline()
		line = input_file.readline()
		line = input_file.readline().rstrip('\n')
		while line:
			test_program.append([int(n) for n in line.split(' ')])
			line = input_file.readline().rstrip('\n')

	return samples, test_program


# Every instruction consists of four values: an opcode, two inputs (named A and B), and an output (named C)
# Addition:
def addr(a, b, c, register):
	"""
	(add register) stores into register C the result of adding register A and register B.
	"""
	register[c] = register[a] + register[b]


def addi(a, b, c, register):
	"""
	(add immediate) stores into register C the result of adding register A and value B.
	"""
	register[c] = register[a] + b


# Multiplication:
def mulr(a, b, c, register):
	"""
	(multiply register) stores into register C the result of multiplying register A and register B.
	"""
	register[c] = register[a] * register[b]


def muli(a, b, c, register):
	"""
	(multiply immediate) stores into register C the result of multiplying register A and value B.
	"""
	register[c] = register[a] * b


# Bitwise AND:
def banr(a, b, c, register):
	"""
	(bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
	"""
	register[c] = register[a] & register[b]


def bani(a, b, c, register):
	"""
	(bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
	"""
	register[c] = register[a] & b


# Bitwise OR:
def borr(a, b, c, register):
	""""
	(bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
	"""
	register[c] = register[a] | register[b]


def bori(a, b, c, register):
	"""
	(bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
	"""
	register[c] = register[a] | b


# Assignment:
def setr(a, b, c, register):
	"""
	(set register) copies the contents of register A into register C. (Input B is ignored.)
	"""
	register[c] = register[a]


def seti(a, b, c, register):
	"""
	(set immediate) stores value A into register C. (Input B is ignored.)
	"""
	register[c] = a


# Greater-than testing:
def gtir(a, b, c, register):
	"""(
	greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if a > register[b] else 0


def gtri(a, b, c, register):
	"""
	(greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if register[a] > b else 0


def gtrr(a, b, c, register):
	"""
	(greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if register[a] > register[b] else 0


# Equality testing:
def eqir(a, b, c, register):
	"""
	(equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if a == register[b] else 0


def eqri(a, b, c, register):
	"""
	(equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if register[a] == b else 0


def eqrr(a, b, c, register):
	"""
	(equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
	"""
	register[c] = 1 if register[a] == register[b] else 0
