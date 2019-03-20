from collections import defaultdict


def part1():
	"""
	How many tiles can the water reach within the range of y values in your scan?
	"""
	ground_slice = run_sim()
	# ground_slice.print_slice()
	print(ground_slice.get_water())


def part2():
	"""
	How many water tiles are left after all remaining water not at rest has drained?
	"""
	ground_slice = run_sim()
	# ground_slice.print_slice()
	print(ground_slice.get_water(True))


def run_sim():
	scan_grid, min_x, max_x = read_input()
	min_y = min(scan_grid.keys())
	max_y = max(scan_grid.keys())
	ground_slice = Ground(scan_grid, min_x, max_x, min_y, max_y)
	ground_slice.flow_water()
	return ground_slice


def read_input():
	# y=1701, x=598..614
	# x=645, y=10..33
	scan_grid = defaultdict(lambda: defaultdict(lambda: '.'))
	min_x = 500
	max_x = 500
	with open('input/day17.txt') as input_file:
		for line in input_file:
			line = line.rstrip('\n')
			parts = line.split(', ')
			clay_constant = int(parts[0][2:])
			clay_range = [int(n) for n in parts[1][2:].split('..')]
			for r in range(clay_range[0], clay_range[1]+1):
				if parts[0][0] == 'x':
					scan_grid[r][clay_constant] = '#'
					min_x = min(clay_constant, min_x)
					max_x = max(clay_constant, max_x)
				else:
					scan_grid[clay_constant][r] = '#'
					min_x = min(r, min_x)
					max_x = max(r, max_x)
	return scan_grid, min_x-1, max_x+1


class Ground:

	def __init__(self, scan_grid, min_x, max_x, min_y, max_y):
		self.scan_grid = scan_grid
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y
		self.sources = [(500, min_y)]

	def get_water(self, settled_only=False):
		water = sum(list(row.values()).count('~') for row in self.scan_grid.values())
		if not settled_only:
			water += sum(list(row.values()).count('|') for row in self.scan_grid.values())
		return water

	def flow_water(self):
		while len(self.sources) > 0:
			x, y = self.sources.pop()
			self.trickle_down(x, y)

	def trickle_down(self, x, y):
		if y > self.max_y:
			return '|'
		current_char = self.scan_grid[y][x]
		if current_char in ['#', '|', '~']:
			return current_char
		# if current_char != '+':
		self.scan_grid[y][x] = '|'
		below = self.trickle_down(x, y+1)
		if below in ['#', '~']:
			left = self.trickle_sideways(x-1, y, -1)
			right = self.trickle_sideways(x+1, y, 1)
			if left == '#' and right == '#':
				self.settle_water(x, y, 1)
				self.settle_water(x, y, -1)
				return '~'
			return '|'
		assert below == '|'
		return '|'

	def trickle_sideways(self, x, y, direction):
		current_char = self.scan_grid[y][x]
		# assert current_char in ['#', '|', '.']
		if current_char == '#':
			return current_char
		if current_char == '.':
			self.scan_grid[y][x] = '|'
		below = self.scan_grid[y+1][x]
		if below in ['#', '~']:
			return self.trickle_sideways(x + direction, y, direction)
		self.scan_grid[y][x] = '+'
		self.sources.append((x, y))
		return '|'

	def settle_water(self, x, y, direction):
		current_char = self.scan_grid[y][x]
		if current_char == '#':
			return
		if self.scan_grid[y-1][x] == '|':
			self.scan_grid[y-1][x] = '+'
			self.sources.append((x, y-1))
		self.scan_grid[y][x] = '~'
		self.settle_water(x + direction, y, direction)

	def print_slice(self):
		for y in range(self.max_y+1):
			res = []
			for x in range(self.min_x, self.max_x+1):
				res.append(self.scan_grid[y][x])
			print(''.join(res))
