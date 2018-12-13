
def part1():
	"""
	Each fuel cell has a coordinate ranging from 1 to 300 in both the X (horizontal) and Y (vertical) direction.
	The power level in a given fuel cell can be found through the following process:
		- Find the fuel cell's rack ID, which is its X coordinate plus 10.
		- Begin with a power level of the rack ID times the Y coordinate.
		- Increase the power level by the value of the grid serial number (your puzzle input).
		- Set the power level to itself multiplied by the rack ID.
		- Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
		- Subtract 5 from the power level.

	What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power?
	"""
	with open('input/day11.txt') as input_file:
		grid_serial = int(input_file.readline())

	power_grid = PowerGrid(grid_serial)
	print(power_grid.get_max_power_square_coordinate())


def part2():
	"""
	You now must find the square of any size with the largest total power.
	What is the X,Y,size identifier of the square with the largest total power?
	"""
	with open('input/day11.txt') as input_file:
		grid_serial = int(input_file.readline())

	power_grid = PowerGrid(grid_serial)
	grid_size = power_grid.grid_size

	max_value = 0
	max_value_size = 1
	max_pos = (0, 0)
	# Each entry in area_sums is the sum of all values of the rectangle for which this position is the lower-right corner
	# Find the maximum single value while we're at it
	area_sums = [[0 for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]
	for y in range(grid_size):
		for x in range(grid_size):
			new_value = power_grid.grid[y][x]
			if new_value > max_value:
				max_value = new_value
				max_pos = (x+1, y+1)
			area_sums[y + 1][x + 1] = new_value + area_sums[y+1][x] + area_sums[y][x+1] - area_sums[y][x]

	for s in range(2, grid_size + 1):
		# print("Handling size", s)
		for y in range(grid_size - s + 1):
			for x in range(grid_size - s + 1):
				area_value = area_sums[y][x] + area_sums[y+s][x+s] - area_sums[y][x+s] - area_sums[y+s][x]
				if area_value > max_value:
					max_value = area_value
					max_value_size = s
					max_pos = (x+1, y+1)

	print(",".join([str(max_pos[0]), str(max_pos[1]), str(max_value_size)]))


class PowerGrid:

	def __init__(self, grid_serial):
		self.grid_serial = grid_serial

		self.grid_size = 300
		# Create the grid
		self.grid = []
		for y in range(1, self.grid_size + 1):
			self.grid.append([])
			for x in range(1, self.grid_size + 1):
				rack_id = x + 10
				power_level = (rack_id * y + grid_serial) * rack_id  # Steps 1-4
				power_level = int(str(power_level)[-3]) - 5  # Steps 5 and 6
				self.grid[y - 1].append(power_level)

	def get_max_power_square_coordinate(self, square_size=3):
		max_power = 0
		max_power_coordinate = (0, 0)
		for y in range(self.grid_size - square_size + 1):
			for x in range(self.grid_size - square_size + 1):
				square_power = self.get_power_square(x, y, square_size)
				if square_power > max_power:
					max_power = square_power
					max_power_coordinate = (x + 1, y + 1)
		return max_power_coordinate

	def get_power_square(self, x, y, square_size=3):
		return sum(sum(self.grid[y2][x:x + square_size]) for y2 in range(y, y + square_size))
