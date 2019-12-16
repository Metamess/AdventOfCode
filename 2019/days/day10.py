from math import atan2
from math import pi
from collections import defaultdict


def part1():
	"""
	A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them.
	This line of sight can be at any angle, not just lines aligned to the grid or diagonally.
	The best location is the asteroid that can detect the largest number of other asteroids.
	How many other asteroids can be detected from that location?
	"""
	field = read_input()
	max_value = 0
	infinity = "inf"
	for j, row in enumerate(field):
		for i, asteroid in enumerate(row):
			if asteroid == '.':
				continue
			positive_angles = []
			negative_angles = []
			for y, row2 in enumerate(field):
				for x, other in enumerate(row2):
					if other == '.':
						continue
					d_y = y-j
					d_x = x-i
					if d_y == 0:
						if d_x == 0:
							continue
						elif d_x > 0:
							if infinity not in positive_angles:
								positive_angles.append(infinity)
						else:
							if infinity not in negative_angles:
								negative_angles.append(infinity)
					elif d_y > 0:
						angle = d_x / d_y
						if angle not in positive_angles:
							positive_angles.append(angle)
					else:
						angle = d_x / d_y
						if angle not in negative_angles:
							negative_angles.append(angle)
			# print(i, j, positive_angles, negative_angles)
			max_value = max(max_value, len(positive_angles) + len(negative_angles))
			# if len(positive_angles) + len(negative_angles) == max_value:
			# 	print(i, j)
	print(max_value)


def part2():
	"""
	The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.
	If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation.
	The Elves are placing bets on which will be the 200th asteroid to be vaporized.
	What do you get if you multiply its X coordinate by 100 and then add its Y coordinate?
	"""
	position_x = 20  # Taken from part 1
	position_y = 20
	angles = defaultdict(list)
	coords = dict()
	field = read_input()
	for y, row in enumerate(field):
		for x, other in enumerate(row):
			if other == '.':
				continue
			d_y = -(y - position_y)
			d_x = x - position_x
			if d_y == 0 and d_x == 0:
				continue
			angle = atan2(d_x, d_y)
			if angle < 0:
				angle += 2*pi
			dist = d_x**2 + d_y**2
			angles[angle].append(dist)
			coords[(angle, dist)] = (x, y)
	order = sorted(list(angles.keys()))
	for a in angles:
		angles[a].sort()
	i = 0
	while i < 200:
		for a in order:
			if angles[a]:
				d = angles[a].pop(0)
				i += 1
				if i == 200:
					c = coords[(a, d)]
					print(c[0]*100 + c[1])
					break


def read_input():
	field = []
	with open('input/day10.txt') as input_file:
		for line in input_file:
			field.append(line.strip())
	return field
