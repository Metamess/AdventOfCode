from collections import defaultdict


def part1():
	"""
	Two wires are connected to a central port and extend outward on a grid.
	What is the Manhattan distance from the central port to the closest intersection?
	"""
	wires = read_input()
	grid = defaultdict(set)

	for w, wire in enumerate(wires):
		position = (0, 0)
		for trace in wire:
			direction = trace[0]
			length = int(trace[1:])
			for i in range(length):
				if direction == "U":
					position = (position[0], position[1] + 1)
				elif direction == "D":
					position = (position[0], position[1] - 1)
				elif direction == "R":
					position = (position[0] + 1, position[1])
				elif direction == "L":
					position = (position[0] - 1, position[1])
				grid[position].add(w)
	min_distance = 99999999
	for k in grid:
		if len(grid[k]) == 2:
			min_distance = min(min_distance, abs(k[0]) + abs(k[1]))
	print(min_distance)


def part2():
	"""
	What is the fewest combined steps the wires must take to reach an intersection?
	"""
	wires = read_input()
	grid = {}

	for w, wire in enumerate(wires):
		l = 0
		position = (0, 0)
		for trace in wire:
			direction = trace[0]
			length = int(trace[1:])
			for i in range(length):
				l += 1
				if direction == "U":
					position = (position[0], position[1] + 1)
				elif direction == "D":
					position = (position[0], position[1] - 1)
				elif direction == "R":
					position = (position[0] + 1, position[1])
				elif direction == "L":
					position = (position[0] - 1, position[1])
				if position not in grid:
					grid[position] = [999999999, 999999999]
				grid[position][w] = min(grid[position][w], l)
	min_distance = 99999999
	for k in grid:
		min_distance = min(min_distance, grid[k][0] + grid[k][1])
	print(min_distance)


def read_input():
	wires = []
	with open('input/day3.txt') as input_file:
		for line in input_file:
			wires.append(line.split(','))
	return wires
