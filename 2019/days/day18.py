from functools import reduce
from collections import defaultdict


def add_points(a, b):
    return a[0] + b[0], a[1] + b[1]


class Intersection:

    def __init__(self, position, previous, direction_to_previous, distance_to_previous, doors_to_previous):
        self.position = position
        self.directions_to_previous = [direction_to_previous]
        self.previous_intersections = {}
        if previous:
            self.previous_intersections[previous] = distance_to_previous
        self.doors_to_previous = doors_to_previous
        self.available_keys = {}

    def add_previous(self, previous, direction_to_previous, distance_to_previous, doors_to_previous):
        if previous in self.previous_intersections:
            # Found the same intersection through 2 direct paths from the same parent, keep the shortest
            if self.previous_intersections[previous] > distance_to_previous:
                self.previous_intersections[previous] = distance_to_previous
                self.directions_to_previous.append(direction_to_previous)
        else:
            self.previous_intersections[previous] = distance_to_previous
            self.directions_to_previous.append(direction_to_previous)
            self.doors_to_previous.extend(doors_to_previous)
            for key_char in self.available_keys:
                previous.propagate_key(key_char, distance_to_previous + self.available_keys[key_char])

    def propagate_key(self, key_char, distance):
        if key_char in self.available_keys:
            if distance >= self.available_keys[key_char]:
                return
        self.available_keys[key_char] = distance
        for prev in self.previous_intersections:
            prev.propagate_key(key_char, distance + self.previous_intersections[prev])

    def find_a_to_b(self, a, b):
        if a in self.available_keys and b in self.available_keys:
            return self.available_keys[a] + self.available_keys[b]
        else:
            return min(prev.find_a_to_b(a, b) for prev in self.previous_intersections)

    def doors_to_start(self, doors):
        doors.extend(self.doors_to_previous)
        for prev in self.previous_intersections:
            return prev.doors_to_start(doors)
        return doors

    def __repr__(self):
        return "X" + str(self.position)


class Maze:

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    reverse = {(0, -1): (0, 1), (0, 1): (0, -1), (-1, 0): (1, 0), (1, 0): (-1, 0)}

    def __init__(self, maze):
        self.maze = maze
        self.intersections = {}
        self.queue = []
        self.keys = {}

    def get_maze_value(self, pos):
        return self.maze[pos[1]][pos[0]]

    def find_next_intersection(self, position, direction, parent_intersection, distance, doors):
        char = self.get_maze_value(position)
        if char == '#':
            # Hit a wall
            return
        elif ord('a') <= ord(char) <= ord('z'):
            # Found a key, treat as intersection
            intersect = Intersection(position, parent_intersection, direction, distance, doors)
            intersect.propagate_key(char, 0)
            self.keys[char] = intersect
            return intersect
        elif ord('A') <= ord(char) <= ord('Z'):
            doors.append(char)
        if position in self.intersections:
            # Found existing intersection
            other = self.intersections[position]
            if self.queue.index(other) > self.queue.index(parent_intersection):
                other.add_previous(parent_intersection, direction, distance, doors)
        else:
            # Check if this is a new intersection
            possibilities = []
            for next_direction in Maze.directions:
                if next_direction != direction and self.get_maze_value(add_points(position, next_direction)) != '#':
                    possibilities.append(next_direction)
            if len(possibilities) > 1:
                # Found new intersection
                return Intersection(position, parent_intersection, direction, distance, doors)
            elif len(possibilities) == 1:
                return self.find_next_intersection(add_points(position, possibilities[0]), Maze.reverse[possibilities[0]], parent_intersection, distance + 1, doors)

    def explore_maze(self, start):
        self.intersections = {start.position: start}
        self.keys = {'@': start}
        self.queue = [start]
        q_i = 0
        while q_i < len(self.queue):
            current_node = self.queue[q_i]
            for dirs in Maze.directions:
                if dirs in current_node.directions_to_previous:
                    continue
                next_node = self.find_next_intersection(add_points(current_node.position, dirs), Maze.reverse[dirs], current_node, 1, [])
                if next_node:
                    self.intersections[next_node.position] = next_node
                    self.queue.append(next_node)
            q_i += 1
        return self.keys


def part1():
    """
    You generate a map of the tunnels (your puzzle input).
    Only one entrance (marked @) is present among the open passages (marked .) and stone walls (#),
    but you also detect an assortment of keys (shown as lowercase letters) and doors (shown as uppercase letters).
    Keys of a given letter open the door of the same letter
    How many steps is the shortest path that collects all of the keys?
    """
    # Phase 1: Pre-processing the input into graph and constraints
    input_maze = read_input()
    maze = Maze(input_maze)

    start = None
    for j, key_char in enumerate(input_maze):
        i = key_char.find('@')
        if i >= 0:
            start = Intersection((i, j), None, None, 0, [])
            start.propagate_key('@', 0)
            break
    assert start

    keys = maze.explore_maze(start)

    locks = {}
    distances = []
    for key_char in sorted(keys.keys()):
        dists = []
        for other_key in sorted(keys.keys()):
            dists.append(keys[key_char].find_a_to_b(key_char, other_key))
        distances.append(dists)
        locks[key_char] = sorted(keys[key_char].doors_to_start([]))

    # Phase 2: Finding the shortest route using dynamic programming
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime_locks = {ord(k) - ord('a') + 1: reduce((lambda x, y: x * y), [1] + [primes[ord(d) - ord('A') + 1] for d in locks[k]]) for k in locks if k is not '@'}
    layer = {(1, 0): 0}

    def get_available(product):
        res = []
        for k in prime_locks:
            if product % primes[k] != 0 and product % prime_locks[k] == 0:
                res.append(k)
        return res

    while True:
        next_layer = defaultdict(lambda: 99999999)
        for (prod, last_key), dist in layer.items():
            available = get_available(prod)
            if len(available) == 0:
                break
            for next_key in available:
                new_dist = distances[last_key][next_key]
                next_tuple = (prod * primes[next_key], next_key)
                next_layer[next_tuple] = min(next_layer[next_tuple], dist + new_dist)
        if len(next_layer) == 0:
            break
        layer = next_layer
    print(min(layer.values()))


def part2():
    """
    You arrive at the vault only to discover that there is not one vault, but four - each with its own entrance.
    Update your map to instead use the correct data.
    you deploy four remote-controlled robots. Each starts at one of the entrances (@).
    Your goal is still to collect all of the keys in the fewest steps, but now, each robot has its own position and can move independently.
    You can only remotely control a single robot at a time.
    What is the fewest steps necessary to collect all of the keys?
    """
    # Phase 1: Pre-processing the input into graph and constraints
    input_maze = read_input()

    start_x = 0
    start_y = 0
    for j, key_char in enumerate(input_maze):
        i = key_char.find('@')
        if i >= 0:
            start_x, start_y = i, j
            break
    input_maze[start_y-1] = input_maze[start_y-1][:start_x - 1] + "@#@" + input_maze[start_y-1][start_x + 2:]
    input_maze[start_y] = input_maze[start_y][:start_x - 1] + "###" + input_maze[start_y][start_x + 2:]
    input_maze[start_y + 1] = input_maze[start_y + 1][:start_x - 1] + "@#@" + input_maze[start_y + 1][start_x + 2:]

    maze = Maze(input_maze)

    start_locations = []
    for j, key_char in enumerate(input_maze):
        i = 0
        while True:
            i = key_char.find('@', i)
            if i < 0:
                break
            new_start = Intersection((i, j), None, None, 0, [])
            new_start.propagate_key('@', 0)
            start_locations.append(new_start)
            i += 1

    keys_per_area = []
    for start in start_locations:
        keys_per_area.append(maze.explore_maze(start))

    locks = {}  # Locks are global
    areas = []
    for keys in keys_per_area:
        list_of_keys = sorted(keys.keys())
        distances = []
        for key_char in list_of_keys:
            dists = []
            for other_key in list_of_keys:
                dists.append(keys[key_char].find_a_to_b(key_char, other_key))
            distances.append(dists)
            locks[key_char] = sorted(keys[key_char].doors_to_start([]))
        key_digits = [ord(k) - ord('a') + 1 if k is not '@' else 0 for k in list_of_keys]
        areas.append({"keys": key_digits, "distances": distances})

    # Phase 2: Finding the shortest route using dynamic programming
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime_locks = {ord(k) - ord('a') + 1: reduce((lambda x, y: x * y), [1] + [primes[ord(d) - ord('A') + 1] for d in locks[k]]) for k in locks if k is not '@'}

    layer = {tuple([1] + list(0 for _ in areas)): 0}

    def get_available(product):
        res = []
        for k in prime_locks:
            if product % primes[k] != 0 and product % prime_locks[k] == 0:
                res.append(k)
        return res

    while True:
        next_layer = defaultdict(lambda: 99999999)
        for (prod, *last_keys), dist in layer.items():
            available = get_available(prod)
            if len(available) == 0:
                break
            for next_key in available:
                new_dist = -1
                next_keys = []
                for i, area in enumerate(areas):
                    if next_key in area["keys"]:
                        last_key = last_keys[i]
                        new_dist = area["distances"][area["keys"].index(last_key)][area["keys"].index(next_key)]
                        next_keys = [next_key if k is i else last_keys[k] for k in range(len(last_keys))]
                        break
                assert new_dist >= 0 and len(next_keys) > 0
                next_tuple = tuple([prod * primes[next_key]] + next_keys)
                next_layer[next_tuple] = min(next_layer[next_tuple], dist + new_dist)
        if len(next_layer) == 0:
            break
        layer = next_layer
    print(min(layer.values()))


def read_input():
    maze = []
    with open('input/day18.txt') as input_file:
        for line in input_file:
            maze.append(line.strip())
    return maze
