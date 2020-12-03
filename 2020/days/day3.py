from functools import reduce


def part1():
    """
    Trees in this area only grow on exact integer coordinates in a grid.
    You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
    The same pattern repeats to the right
    Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
    """
    grid = read_input()
    trees = 0
    x = 0
    for line in grid:
        if line[x] == '#':
            trees += 1
        x = (x + 3) % len(line)
    print(trees)


def part2():
    """
    Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
        Right 1, down 1.
        Right 3, down 1. (This is the slope you already checked.)
        Right 5, down 1.
        Right 7, down 1.
        Right 1, down 2.
    What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    """
    grid = read_input()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_at_slopes = []
    for right, down in slopes:
        x = 0
        trees = 0
        for y, line in enumerate(grid):
            if y % down != 0:
                continue
            if line[x] == '#':
                trees += 1
            x = (x + right) % len(line)
        trees_at_slopes.append(trees)
    print(reduce((lambda a, b: a*b), trees_at_slopes))


def read_input():
    grid = []
    with open('input/day3.txt') as input_file:
        for line in input_file:
            grid.append(line.rstrip())
    return grid
