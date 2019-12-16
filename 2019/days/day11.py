from . import computer


def part1():
	"""
	Provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will output two values:
	First, it will output a value indicating the color to paint the panel the robot is over: 0 means black, and 1 means white.
	Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
	After the robot turns, it should always move forward exactly one panel.
	The robot starts facing up.
	How many panels does it paint at least once?
	"""
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	position = (0, 0)
	direction = 0
	panels = dict()
	input_value = []
	comp = computer.get_computer(read_input(), input_value)
	while True:
		# Provide input
		if position in panels:
			input_value.append(panels[position])
		else:
			input_value.append(0)
		# Run robot
		color = next(comp)
		if type(color) == list:
			break
		# Paint
		panels[position] = color
		delta_dir = next(comp)
		direction = (direction + int((delta_dir - 0.5)*2)) % 4
		# Move
		position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
	print(len(panels))


def part2():
	"""
	After starting the robot on a single white panel instead, what registration identifier does it paint on your hull?
	"""
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	position = (0, 0)
	direction = 0
	panels = {(0, 0): 1}
	input_value = []
	comp = computer.get_computer(read_input(), input_value)
	while True:
		# Provide input
		if position in panels:
			input_value.append(panels[position])
		else:
			input_value.append(0)
		# Run robot
		color = next(comp)
		if type(color) == list:
			break
		# Paint
		panels[position] = color
		delta_dir = next(comp)
		direction = (direction + int((delta_dir - 0.5) * 2)) % 4
		# Move
		position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
	min_x = 9999999
	min_y = 9999999
	max_x = -9999999
	max_y = -9999999
	for coord in panels:
		min_x = min(min_x, coord[0])
		min_y = min(min_y, coord[1])
		max_x = max(max_x, coord[0])
		max_y = max(max_y, coord[1])
	width = max_x - min_x + 1
	height = max_y - min_y + 1
	hull = [[' ' for i in range(width)] for j in range(height)]
	for coord in panels:
		if panels[coord] == 1:
			hull[coord[1]-min_y][coord[0]-min_x] = '#'
	for row in hull[::-1]:
		print(''.join(row))


def read_input():

	with open('input/day11.txt') as input_file:
		return [int(x) for x in input_file.readline().split(',')]
