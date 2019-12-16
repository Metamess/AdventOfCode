from functools import reduce


def part1():
	"""
	you calculate the position of each moon (your puzzle input). You just need to simulate their motion so you can avoid them.
	Each moon has a 3-dimensional position (x, y, and z) and a 3-dimensional velocity.
	Within each time step, first update the velocity of every moon by applying gravity.
	To apply gravity, consider every pair of moons. On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together.
	Once all gravity has been applied, apply velocity.

	Then, it might help to calculate the total energy in the system.
	The total energy for a single moon is its potential energy multiplied by its kinetic energy.
	A moon's potential energy is the sum of the absolute values of its x, y, and z position coordinates.
	A moon's kinetic energy is the sum of the absolute values of its velocity coordinates.
	What is the total energy in the system after simulating the moons given in your scan for 1000 steps?
	"""
	moons = read_input()
	velocities = [[0, 0, 0] for moon in moons]
	time = 0
	end_time = 1000
	while time < end_time:
		gravities = [[0, 0, 0] for moon in moons]
		for i, moon in enumerate(moons):
			for other in moons:
				for axis in range(len(moon)):
					if moon[axis] < other[axis]:
						gravities[i][axis] += 1
					elif moon[axis] > other[axis]:
						gravities[i][axis] -= 1
		for i, moon in enumerate(moons):
			for axis in range(3):
				velocities[i][axis] += gravities[i][axis]
				moon[axis] += velocities[i][axis]
		time += 1
	energy = 0
	for i, moon in enumerate(moons):
		potential = sum([abs(d) for d in moon])
		kinetic = sum(abs(d) for d in velocities[i])
		energy += potential * kinetic
	print(energy)


def part2():
	"""

	"""
	moons = read_input()
	loop_sizes = [0, 0, 0]
	states = [dict() for _ in range(3)]
	velocities = [[0, 0, 0] for _ in moons]
	time = 0
	while loop_sizes.count(0) > 0:
		gravities = [[0, 0, 0] for _ in moons]
		for i, moon in enumerate(moons):
			for other in moons:
				for axis in range(len(moon)):
					if moon[axis] < other[axis]:
						gravities[i][axis] += 1
					elif moon[axis] > other[axis]:
						gravities[i][axis] -= 1
		for i, moon in enumerate(moons):
			for axis in range(3):
				velocities[i][axis] += gravities[i][axis]
				moon[axis] += velocities[i][axis]
				# check combos
		for axis in range(3):
			if loop_sizes[axis]:
				continue
			state = []
			for i, moon in enumerate(moons):
				state.append(moon[axis])
				state.append(velocities[i][axis])
			if str(state) in states[axis]:
				loop_sizes[axis] = time - states[axis][str(state)]
				# print(axis, state)
			else:
				states[axis][str(state)] = time
		time += 1
	print(reduce(lcm, loop_sizes))


def read_input():
	moons = []
	with open('input/day12.txt') as input_file:
		for line in input_file:
			moons.append([int(d[2:]) for d in line.strip()[1:-1].split(', ')])
	return moons


def gcd(x, y):
	while y:
		x, y = y, x % y
	return x


def lcm(x, y):
	return x*y // gcd(x, y)
