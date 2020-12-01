from collections import defaultdict
from copy import deepcopy
from typing import List, Any, Union, Tuple


def part1():
    """
    This map of the maze shows solid walls (#) and open passages (.).
    Every maze on Pluto has a start (the open tile next to AA) and an end (the open tile next to ZZ).
    Mazes on Pluto also have portals; When on an open tile next to one of these labels, a single step can take you to the other tile with the same label.
    How many steps does it take to get from the open tile marked AA to the open tile marked ZZ?
    """
    maze = read_input()
    start, portals = get_portals(maze)

    distance = 0
    current_list = [start]
    solution = 0
    while not solution:
        next_list = []
        for y, x in current_list:
            neighbours = [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]
            maze[y][x] = distance % 10
            for neighbour_y, neighbour_x in neighbours:
                neighbour_char = maze[neighbour_y][neighbour_x]
                if neighbour_char == '.':
                    next_list.append((neighbour_y, neighbour_x))
                elif neighbour_char == '#':
                    continue
                elif type(neighbour_char) == int:
                    continue
                else:
                    assert ord('A') <= ord(neighbour_char) <= ord('Z')
                    other_side = portals[(y, x)]
                    if other_side == "ZZ":
                        solution = distance
                        break
                    elif maze[other_side[0]][other_side[1]] == '.':
                        next_list.append(other_side)
                    else:
                        assert type(maze[other_side[0]][other_side[1]]) == int
        current_list = next_list
        distance += 1
    # for row in maze:
    #     print(''.join([str(c) for c in row]))
    print(solution)


def get_portals(maze):
    portals = defaultdict(list)
    for y, row in enumerate(maze[1:-1], 1):
        for x, char in enumerate(row[1:-1], 1):
            if ord('A') <= ord(char) <= ord('Z'):
                if maze[y - 1][x] == '.':  # A bottom portal
                    label = char + maze[y + 1][x]
                    coordinate = (y - 1, x)
                elif maze[y + 1][x] == '.':  # A top portal
                    label = maze[y - 1][x] + char
                    coordinate = (y + 1, x)
                elif maze[y][x - 1] == '.':  # A left portal
                    label = char + maze[y][x + 1]
                    coordinate = (y, x - 1)
                elif maze[y][x + 1] == '.':  # a right portal
                    label = maze[y][x - 1] + char
                    coordinate = (y, x + 1)
                else:
                    continue
                portals[label].append(coordinate)

    portal_to_portal = {}
    start = None
    for label in portals:
        if label == "AA":
            assert len(portals[label]) == 1
            start = portals[label][0]
            portal_to_portal[portals[label][0]] = portals[label][0]
        elif label == "ZZ":
            assert len(portals[label]) == 1
            portal_to_portal[portals[label][0]] = "ZZ"
        else:
            assert len(portals[label]) == 2
            portal_to_portal[portals[label][0]] = portals[label][1]
            portal_to_portal[portals[label][1]] = portals[label][0]
    return start, portal_to_portal


def part2():
    """
    The marked connections in the maze aren't portals: they physically connect to a larger or smaller copy of the maze.
    Specifically, the labeled tiles around the inside edge actually connect to a smaller copy of the same maze,
    and the smaller copy's inner labeled tiles connect to yet a smaller copy, and so on.
    When you enter the maze, you are at the outermost level;
    When accounting for recursion, how many steps does it take to get from the open tile marked AA to the open tile marked ZZ, both at the outermost layer?
    """
    original_maze = read_input()
    start, portals = get_portals(original_maze)
    left_wall = len(original_maze[2])-3
    bottom_wall = len(original_maze)-3

    def is_outer_portal(y, x):
        return y == 2 or y == bottom_wall or x == 2 or x == left_wall

    distance = 0
    mazes = [deepcopy(original_maze)]
    current_list = [(start[0], start[1], 0)]  # The third item denotes the recursion level
    solution = 0
    while not solution:
        next_list = []
        for y, x, level in current_list:
            neighbours = [(y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x)]
            mazes[level][y][x] = distance % 10
            for neighbour_y, neighbour_x in neighbours:
                neighbour_char = mazes[level][neighbour_y][neighbour_x]
                if neighbour_char == '.':
                    next_list.append((neighbour_y, neighbour_x, level))
                elif neighbour_char == '#':
                    continue
                elif type(neighbour_char) == int:
                    continue
                else:
                    assert ord('A') <= ord(neighbour_char) <= ord('Z')  # We're at a portal
                    other_side = portals[(y, x)]
                    if other_side == start or (other_side == "ZZ" and level != 0):
                        continue
                    elif other_side == "ZZ":
                        solution = distance
                        break
                    else:
                        outer = is_outer_portal(y, x)
                        if level == 0 and outer:  # We can't go into negative levels
                            continue
                        if not outer and level == len(mazes)-1:  # Make new level
                            mazes.append(deepcopy(original_maze))
                        next_level = level - 1 if outer else level + 1
                        neighbour_char = mazes[next_level][other_side[0]][other_side[1]]
                        if neighbour_char == '.':
                            next_list.append((other_side[0], other_side[1], next_level))
                        else:
                            assert type(neighbour_char) == int
        current_list = next_list
        distance += 1
    # for level, maze in enumerate(mazes):
    #     print("level", level)
    #     for row in maze:
    #         print(''.join([str(c) for c in row]))
    print(solution)


def read_input():
    maze = []
    with open('input/day20.txt') as input_file:
        for line in input_file:
            maze.append(list(line.rstrip()) + [' ', ' '])
    return maze
