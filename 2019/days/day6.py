
def part1():
	"""
	Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object.
	In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".
	What is the total number of direct and indirect orbits in your map data?
	"""
	orbits = read_input()
	res = 0
	for thing in orbits:
		while thing != "COM":
			res += 1
			thing = orbits[thing]
	print(res)


def part2():
	"""
	What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting?
	(Between the objects they are orbiting - not between YOU and SAN.)
	"""
	orbits = read_input()
	my_line = []
	thing = "YOU"
	while thing != "COM":
		my_line.append(orbits[thing])
		thing = orbits[thing]
	santa_line = []

	thing = "SAN"
	while thing != "COM":
		santa_line.append(orbits[thing])
		thing = orbits[thing]

	same = 0
	while True:
		same += 1
		if my_line[-same] != santa_line[-same]:
			same -= 1
			break

	print(len(my_line) + len(santa_line) - 2*same)


def read_input():
	orbits = {}
	with open('input/day6.txt') as input_file:
		for line in input_file:
			a, b = line[:-1].split(')')
			orbits[b] = a
	return orbits
