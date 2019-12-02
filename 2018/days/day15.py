from copy import deepcopy
from operator import attrgetter


# Underscores make for easier reading with fonts with variable character width
_EMPTY = '_'


def part1():
	"""
	You need to determine the outcome of the battle:
	the number of full rounds that were completed (not counting the round in which combat ends)
	multiplied by the sum of the hit points of all remaining units at the moment combat ends.
	What is the outcome of the combat described in your puzzle input?
	"""
	cave, creatures = read_input()
	print(run_combat(cave, creatures))


def part2():
	"""
	After increasing the Elves' attack power until it is just barely enough for them to win without any Elves dying,
	what is the outcome of the combat described in your puzzle input?
	"""
	attack_power = 3
	outcome = None
	while outcome is None:
		attack_power += 1
		cave, creatures = read_input()
		for creature in creatures:
			if creature.team == 'E':
				creature.ap = attack_power
		outcome = run_combat(cave, creatures, immortal_elves=True)
	print(outcome)


def run_combat(cave, creatures, immortal_elves=False):
	"""
	:return: The hp_sum * round number if combat has ended, or None if immortal_elves is True and an elf died
	"""
	elf_count = sum(1 if creature.team == "E" else 0 for creature in creatures)
	goblin_count = len(creatures) - elf_count
	round_number = 0
	# Run rounds of combat until only one team is left
	while elf_count > 0 and goblin_count > 0:
		# Since we can't delete items from a list we're iterating over, keep track of deceased creatures separately
		deceased_this_round = []
		# Give every creature a turn
		for creature in creatures:
			# If combat ends this round, make sure we don't count it
			if elf_count == 0 or goblin_count == 0:
				round_number -= 1
				break
			# Don't give turns to dead creatures
			if creature in deceased_this_round:
				continue
			# take_turn will return the creature that was killed, if any
			deceased = creature.take_turn(cave, creatures)
			if deceased:
				deceased_this_round.append(deceased)
				cave[deceased.y][deceased.x] = _EMPTY
				if deceased.team == 'E':
					if immortal_elves:
						return
					elf_count -= 1
				else:
					goblin_count -= 1
		# Now we can safely remove dead creatures
		for deceased in deceased_this_round:
			creatures.remove(deceased)
		# Don't forget to update the turn order when creatures have moved
		creatures.sort()
		round_number += 1

	hp_sum = sum(creature.hp for creature in creatures)
	return hp_sum * round_number


def read_input():
	cave = []
	creatures = []
	with open('input/day15.txt') as input_file:
		for y, line in enumerate(input_file):
			cave_line = []
			for x, char in enumerate(line):
				if char == '\n':
					continue
				if char == 'E' or char == 'G':
					creatures.append(Creature(x, y, char))
				if char == '.':
					char = _EMPTY
				cave_line.append(char)
			cave.append(cave_line)
	return cave, creatures


class Point:

	# By keeping to this search order, the results are guaranteed to be in 'reading order'
	search_order = [
		{'x': 0, 'y': -1},
		{'x': -1, 'y': 0},
		{'x': 1, 'y': 0},
		{'x': 0, 'y': 1}]

	def __init__(self, x, y, distance, parent):
		self.x = x
		self.y = y
		self.distance = distance
		self.parent = parent

	def __lt__(self, other):
		if not isinstance(other, Point):
			return NotImplemented
		if other.y > self.y:
			return True
		if other.y == self.y and other.x > self.x:
			return True
		return False


class Creature(Point):

	def __init__(self, x, y, team):
		Point.__init__(self, x, y, 0, None)
		self.team = team
		self.hp = 200
		self.ap = 3

	def __repr__(self):
		return '(' + self.team + " at (" + str(self.x) + ',' + str(self.y) + ") " + str(self.hp) + ')'

	def take_turn(self, cave, creatures):
		"""
		:return: Creature object that this creature killed this turn if any, None otherwise
		"""
		target_location = self.get_target_location(deepcopy(cave))
		if not target_location:
			return

		while target_location.distance > 1:
			target_location = target_location.parent
		# Walk if we have to
		if target_location.distance == 1:
			assert cave[self.y][self.x] == self.team
			cave[self.y][self.x] = _EMPTY
			self.x = target_location.x
			self.y = target_location.y
			assert cave[self.y][self.x] == _EMPTY
			cave[self.y][self.x] = self.team

		return self.attempt_attack(cave, creatures)

	def get_target_location(self, cave_copy):
		"""
		:return: Point object to walk to if any, None otherwise
		"""
		# Find a point to walk to
		targets = []
		next_points = [self]
		while len(next_points) > 0 and len(targets) == 0:
			prev_points = next_points
			next_points = []
			for prev_point in prev_points:
				for direction in Point.search_order:
					next_x = prev_point.x + direction['x']
					next_y = prev_point.y + direction['y']
					next_location_char = cave_copy[next_y][next_x]
					if next_location_char == _EMPTY:
						cave_copy[next_y][next_x] = prev_point.distance + 1
						next_point = Point(next_x, next_y, prev_point.distance + 1, prev_point)
						next_points.append(next_point)
					elif (next_location_char == 'E' or next_location_char == 'G') and next_location_char != self.team:
						targets.append(prev_point)
				if len(targets) > 0:
					break
		return None if not len(targets) else targets[0]

	def attempt_attack(self, cave, creatures):
		"""
		:return: The creature that was killed, or None
		"""
		targets = []
		# Find targets in range
		for direction in Point.search_order:
			other_x = self.x + direction['x']
			other_y = self.y + direction['y']
			other_char = cave[other_y][other_x]
			if (other_char == 'E' or other_char == 'G') and other_char != self.team:
				enemy = next((enemy for enemy in creatures if enemy.x == other_x and enemy.y == other_y), None)
				assert enemy is not None
				targets.append(enemy)
		if not len(targets):
			return

		# Attack!
		target = min(targets, key=attrgetter('hp'))
		target.hp -= self.ap
		if target.hp <= 0:
			return target
		return
