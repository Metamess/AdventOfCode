from itertools import cycle
from operator import attrgetter


def part1():
	"""
	Tracks consist of straight paths (| and -), curves (/ and \), and intersections (+).
	Each time a cart has the option to turn (by arriving at any intersection), it turns left the first time,
	goes straight the second time, turns right the third time, and then repeats those directions
	After following their respective paths for a while, the carts eventually crash.
	To help prevent crashes, you'd like to know the location of the first crash.
	"""
	tracks, carts = read_input()

	# Run the carts along the tracks until there is a collision
	while True:
		carts.sort(key=attrgetter('y', 'x'))
		for cart in carts:
			cart.move(tracks)
			if cart.check_collision(carts):
				print(str(cart.x) + ',' + str(cart.y))
				exit()


def part2():
	"""
	The Elves know where to be in advance and instantly remove the two crashing carts the moment any crash occurs.
	What is the location of the last cart at the end of the first tick where it is the only cart left?
	"""
	tracks, carts = read_input()

	# Run the carts along the tracks until there is only one left
	while len(carts) > 1:
		carts.sort(key=attrgetter('y', 'x'))
		crashed = []
		for cart in carts:
			if cart in crashed:
				continue
			cart.move(tracks)
			other = cart.check_collision(carts)
			if other:
				crashed.append(cart)
				crashed.append(other)
		for cart in crashed:
			carts.remove(cart)
	print(str(carts[0].x) + ',' + str(carts[0].y))


def read_input():
	tracks = []
	carts = []
	with open('input/day13.txt') as input_file:
		for y, line in enumerate(input_file):
			new_track = []
			for x, char in enumerate(line):
				if char in ['>', '<', '^', 'v']:
					carts.append(Cart(x, y, char))
					if char == '>' or char == "<":
						char = '-'
					else:
						char = '|'
				new_track.append(char)
			tracks.append(new_track)
	return tracks, carts


class Cart:

	char_to_dir = {
		'>': 0,
		'^': 1,
		'<': 2,
		'v': 3
	}

	dir_to_delta = {
		0: (1, 0),
		1: (0, -1),
		2: (-1, 0),
		3: (0, 1)
	}

	def __init__(self, x, y, char):
		self.x = x
		self.y = y
		self.direction = Cart.char_to_dir[char]
		self.intersection_action = cycle([1, 0, -1])

	def move(self, tracks):
		dx, dy = Cart.dir_to_delta[self.direction]
		next_track = tracks[self.y + dy][self.x + dx]
		if next_track == '\\':
			self.direction = 3 - self.direction
		elif next_track == '/':
			self.direction += 1 - 2 * (self.direction % 2)
		elif next_track == '+':
			self.direction = (self.direction + self.intersection_action.__next__()) % 4
		self.x += dx
		self.y += dy

	def check_collision(self, carts):
		for other in carts:
			if other is not self and other.x == self.x and other.y == self.y:
				return other
		return None
