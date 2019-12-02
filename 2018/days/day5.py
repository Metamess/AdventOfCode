
def part1():
	"""
	The polymer is formed by smaller units which, when triggered, react with each other such that
	two adjacent units of the same type and opposite polarity are destroyed.
	Units' types are represented by letters;
	units' polarity is represented by capitalization.
	How many units remain after fully reacting the polymer you scanned?
	"""
	with open('input/day5.txt') as f:
		input_polymer = f.readline()

	result_length = collapse_polymer(input_polymer)
	print(result_length)


def part2():
	"""
	What is the length of the shortest polymer you can produce by removing all units of exactly one type
	and fully reacting the result?
	"""
	with open('input/day5.txt') as f:
		input_polymer = f.readline()

	min_length = len(input_polymer)
	for letter in "abcdefghijklmnopqrstuvwxyz":
		min_length = min(collapse_polymer(input_polymer, letter), min_length)
	print(min_length)


def collapse_polymer(input_polymer, skip_molecule=None):
	while input_polymer[0].lower() == skip_molecule:
		input_polymer = input_polymer[1:]
	result_polymer = [input_polymer[0]]
	input_polymer = input_polymer[1:]
	for i, molecule in enumerate(input_polymer):
		if molecule.lower() == skip_molecule:
			continue
		if len(result_polymer) == 0:
			result_polymer.append(molecule)
			continue
		if result_polymer[-1].isupper():
			if molecule.isupper():
				# Two uppercase letters in a row, nothing happens
				result_polymer.append(molecule)
				continue
		elif molecule.islower():
			# Two lowercase letters in a row, nothing happens
			result_polymer.append(molecule)
			continue

		if result_polymer[-1].upper() != molecule.upper():
			# Two different letters in a row, nothing happens
			result_polymer.append(molecule)
			continue

		# The two letters annihilate each other
		result_polymer.pop()
	return len(result_polymer)
