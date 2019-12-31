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


def part1():
    """
    You generate a map of the tunnels (your puzzle input).
    Only one entrance (marked @) is present among the open passages (marked .) and stone walls (#),
    but you also detect an assortment of keys (shown as lowercase letters) and doors (shown as uppercase letters).
    Keys of a given letter open the door of the same letter
    How many steps is the shortest path that collects all of the keys?
    """
    # Phase 1: Pre-processing the input into graph and constraints
    maze = read_input()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    reverse = {(0, -1): (0, 1), (0, 1): (0, -1), (-1, 0): (1, 0), (1, 0): (-1, 0)}

    def get_maze_value(pos):
        return maze[pos[1]][pos[0]]

    def find_next_intersection(position, direction, parent_intersection, distance, doors):
        char = get_maze_value(position)
        if char == '#':
            # Hit a wall
            return
        elif ord('a') <= ord(char) <= ord('z'):
            # Found a key, treat as intersection
            intersect = Intersection(position, parent_intersection, direction, distance, doors)
            intersect.propagate_key(char, 0)
            keys[char] = intersect
            return intersect
        elif ord('A') <= ord(char) <= ord('Z'):
            doors.append(char)
        if position in intersections:
            # Found existing intersection
            other = intersections[position]
            if queue.index(other) > queue.index(parent_intersection):
                other.add_previous(parent_intersection, direction, distance, doors)
        else:
            # Check if this is a new intersection
            possibilities = []
            for next_direction in directions:
                if next_direction != direction and get_maze_value(add_points(position, next_direction)) != '#':
                    possibilities.append(next_direction)
            if len(possibilities) > 1:
                # Found new intersection
                return Intersection(position, parent_intersection, direction, distance, doors)
            elif len(possibilities) == 1:
                return find_next_intersection(add_points(position, possibilities[0]), reverse[possibilities[0]], parent_intersection, distance + 1, doors)

    start = None
    intersections = {}
    for j, key_char in enumerate(maze):
        i = key_char.find('@')
        if i >= 0:
            start = Intersection((i, j), None, None, 0, [])
            start.propagate_key('@', 0)
            intersections[(i, j)] = start
            break
    assert start

    locks = {}
    keys = {'@': start}
    queue = [start]
    q_i = 0
    while q_i < len(queue):
        current_node = queue[q_i]
        for dirs in directions:
            if dirs in current_node.directions_to_previous:
                continue
            next_node = find_next_intersection(add_points(current_node.position, dirs), reverse[dirs], current_node, 1, [])
            if next_node:
                intersections[next_node.position] = next_node
                queue.append(next_node)
        q_i += 1
    # print(keys)
    distances = []
    for key_char in sorted(keys.keys()):
        dists = []
        for other_key in sorted(keys.keys()):
            dists.append(keys[key_char].find_a_to_b(key_char, other_key))
        distances.append(dists)
        locks[key_char] = sorted(keys[key_char].doors_to_start([]))

    # for row in distances:
    #     print(row)
    # print(locks)

    # Phase 2: Finding the shortest route using dynamic programming
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime_locks = {ord(k) - ord('a') + 1 if k is not '@' else 0: reduce((lambda x, y: x * y), [1] + [primes[ord(d) - ord('A') + 1] for d in locks[k]]) for k in locks}
    prime_locks.pop(0)
    # print(prime_locks)
    layer = {(1, 0): 0}

    def get_available(product):
        res = []
        for k in prime_locks:
            if product % primes[k] != 0 and product % prime_locks[k] == 0:
                res.append(k)
        return res

    # print(list(chr(d + ord('a') - 1) for d in get_available(1)))
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
    # print(layer)
    print(min(layer.values()))


def part2():
    """

    """
    pass


def read_input():
    maze = []
    with open('input/day18.txt') as input_file:
        for line in input_file:
            maze.append(line.strip())
    return maze
