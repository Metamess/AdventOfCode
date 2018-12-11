
def part1():
	"""
	Each line represents one point.
	What message will eventually appear in the sky?
	"""
	# Assumption: Points are aligned when point cloud area is smallest
	point_cloud = PointCloud()
	point_cloud.read_input()
	min_area = point_cloud.get_area() + 1
	while True:
		new_area = point_cloud.get_area()
		if new_area > min_area:
			point_cloud.move(-1)
			break
		min_area = new_area
		point_cloud.move(1)
	output_file_path = "output_day10.txt"
	point_cloud.save_to_file(output_file_path)
	print("Area smallest at t=" + str(point_cloud.time))
	print("Result saved to", output_file_path)


def part2():
	"""
	Exactly how many seconds would they have needed to wait for that message to appear?
	"""
	part1()


class PointCloud:

	def __init__(self):
		self.points = []
		self.time = 0

	def read_input(self, file_path="input/day10.txt"):
		with open(file_path) as input_file:
			for line in input_file:
				# position=< 41660,  20869> velocity=<-4, -2>
				x_pos = int(line[10:16])
				y_pos = int(line[18:24])
				x_vel = int(line[36:38])
				y_vel = int(line[40:42])
				self.points.append(Point(x_pos, y_pos, x_vel, y_vel))

	def get_area(self):
		return self.get_width() * self.get_height()

	def get_width(self):
		min_x = min(p.x_position for p in self.points)
		max_x = max(p.x_position for p in self.points)
		return max_x - min_x + 1

	def get_height(self):
		min_y = min(p.y_position for p in self.points)
		max_y = max(p.y_position for p in self.points)
		return max_y - min_y + 1

	def move(self, seconds):
		self.time += seconds
		for point in self.points:
			point.move(seconds)

	def save_to_file(self, file_path="output_day10.txt"):
		min_x = min(p.x_position for p in self.points)
		min_y = min(p.y_position for p in self.points)
		width = self.get_width()
		height = self.get_height()
		grid = [['.' for _ in range(width)] for _ in range(height)]
		for point in self.points:
			grid[point.y_position - min_y][point.x_position - min_x] = '#'
		with open(file_path, 'w+') as output_file:
			for line in grid:
				output_file.write("".join(line) + '\n')


class Point:

	def __init__(self, x_pos, y_pos, x_vel, y_vel):
		self.x_position = x_pos
		self.y_position = y_pos
		self.x_velocity = x_vel
		self.y_velocity = y_vel

	def move(self, seconds=1):
		self.x_position += self.x_velocity * seconds
		self.y_position += self.y_velocity * seconds
