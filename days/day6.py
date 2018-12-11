from collections import defaultdict


def part1():
	"""
	Using only the Manhattan distance, determine the area around each coordinate by counting the number of
	integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).
	What is the size of the largest area that isn't infinite?
	"""
	target_area = TargetArea()
	print(target_area.solve_part1())


def part2():
	"""
	What is the size of the region containing all locations which have
	a total distance to all given coordinates of less than 10000?
	"""
	target_area = TargetArea()
	print(target_area.solve_part2())


class TargetArea:

	def __init__(self, input_path='input/day6.txt'):
		self.coordinate_list = []
		self.min_x = 2 ** 32
		self.min_y = 2 ** 32
		self.max_x = -(2 ** 32)
		self.max_y = -(2 ** 32)
		with open(input_path) as input_coordinates:
			for coordinate in input_coordinates:
				x = int(coordinate.split(', ')[0])
				y = int(coordinate.split(', ')[1])
				self.min_x = min(x, self.min_x)
				self.min_y = min(y, self.min_y)
				self.max_x = max(x, self.max_x)
				self.max_y = max(y, self.max_y)
				self.coordinate_list.append((x, y))
		self.width = self.max_x - self.min_x + 1
		self.height = self.max_y - self.min_y + 1

	def mark_territories(self):
		area = [[(-2, 2 ** 32) for _ in range(self.width)] for _ in range(self.height)]
		# pass over the area to mark territory per coordinate
		for n, coordinate in enumerate(self.coordinate_list):
			corrected_coordinate = (coordinate[0] - self.min_x, coordinate[1] - self.min_y)
			for y in range(self.height):
				for x in range(self.width):
					dist = TargetArea.get_manhattan_dist(x, y, corrected_coordinate[0], corrected_coordinate[1])
					if area[y][x][1] < dist:
						continue
					if area[y][x][1] == dist:
						area[y][x] = (-1, dist)
					else:
						area[y][x] = (n, dist)
		return area

	def get_infinite_areas(self, area):
		# mark infinite areas for removal, i.e. those with area on the borders
		infinite_areas = set()
		for x in range(self.width):
			infinite_areas.add(area[0][x][0])
			infinite_areas.add(area[self.height - 1][x][0])
		for y in range(self.height):
			infinite_areas.add(area[y][0][0])
			infinite_areas.add(area[0][self.width - 1][0])
		return infinite_areas

	def calculate_combined_distances(self):
		area = [[0 for _ in range(self.width)] for _ in range(self.height)]

		for coordinate in self.coordinate_list:
			corrected_coordinate = (coordinate[0] - self.min_x, coordinate[1] - self.min_y)
			for y in range(self.height):
				for x in range(self.width):
					dist = TargetArea.get_manhattan_dist(x, y, corrected_coordinate[0], corrected_coordinate[1])
					area[y][x] += dist
		return area

	def solve_part1(self):
		area = self.mark_territories()
		infinite_areas = self.get_infinite_areas(area)

		area_per_coordinate = defaultdict(int)
		for y in range(self.height):
			for x in range(self.width):
				winner = area[y][x][0]
				if winner not in infinite_areas:
					area_per_coordinate[winner] += 1
		return max(area_per_coordinate.values())

	def solve_part2(self):
		close_position_counter = 0
		area = self.calculate_combined_distances()
		for y in range(self.height):
			for x in range(self.width):
				if area[y][x] < 10000:
					close_position_counter += 1
		return close_position_counter

	@staticmethod
	def get_manhattan_dist(x1, y1, x2, y2):
		return abs(x1 - x2) + abs(y1 - y2)
