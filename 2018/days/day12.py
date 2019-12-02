
def part1():
	"""
	Your puzzle input contains a list of pots from 0 to the right,
	and whether they do (#) or do not (.) currently contain a plant, the initial state.
	For each generation of plants, a given pot has or does not have a plant based on whether that pot
	(and the two pots on either side of it) had a plant in the last generation.
	After 20 generations, what is the sum of the numbers of all pots which contain a plant?
	"""
	plants, rules = read_input()

	for i in range(20):
		plants = grow_generation(plants, rules)

	print(sum(plants))


def part2():
	"""
	After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?
	"""
	plants, rules = read_input()
	last_sum = 0
	for i in range(1, 201):
		plants = grow_generation(plants, rules)
		new_sum = sum(plants)
		# As it turns out, after about 200 iterations, the sum constantly grows 53 per generation
		# print("For generation", i, "the sum is", new_sum, "with a delta of", new_sum - last_sum)
		last_sum = new_sum

	print(last_sum + (50000000000-200) * 53)


def read_input():
	plants = set()
	rules = set()
	# Since the solution depends on counting the indexes of pots with plants, keeping track of just those suffices
	with open('input/day12.txt') as input_file:
		pots_state = input_file.readline()[len('initial state: '):-1]
		assert input_file.readline() == '\n'  # Skip the empty second line
		for i, pot in enumerate(pots_state):
			if pot == '#':
				plants.add(i)

		for line in input_file:
			if line[-2] == '#':
				rules.add(line[:5])
	return plants, rules


def grow_generation(starting_plants, rules):
	resulting_plants = set()

	for center_id in range(min(starting_plants) - 4, max(starting_plants) + 5):
		neighborhood = []
		for pot_id in range(center_id - 2, center_id + 3):
			if pot_id in starting_plants:
				neighborhood.append('#')
			else:
				neighborhood.append('.')

		if ''.join(neighborhood) in rules:
			resulting_plants.add(center_id)

	return resulting_plants
