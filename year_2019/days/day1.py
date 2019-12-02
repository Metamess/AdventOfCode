
def part1():
	"""
	To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
	What is the sum of the fuel requirements for all of the modules on your spacecraft?
	"""
	res = 0
	values = read_input()
	for mass in values:
		res += mass // 3 - 2
	print(res)


def part2():
	"""
	Fuel itself requires fuel just like a module.
	Any mass that would require negative fuel should instead be treated as if it requires zero fuel;
	for each module mass, calculate its fuel and add it to the total.
	What is the sum of the fuel requirements for all of the modules on your spacecraft
	when also taking into account the mass of the added fuel?
	"""
	res = 0
	values = read_input()
	for mass in values:
		while True:
			mass = mass // 3 - 2
			if mass < 0:
				break
			res += mass
	print(res)


def read_input():
	values = []
	with open('input/day1.txt') as input_file:
		for line in input_file:
			values.append(int(line))
	return values
