def part1():
    """
    Expand the universe, then find the length of the shortest path between every pair of galaxies.
    What is the sum of these lengths?
    """
    return solve(1)


def part2():
    """
    """
    return solve(1000000-1)


def solve(distance: int) -> int:
    universe = read_input()
    galaxies = []
    empty_columns = [all(line[i] == "." for line in universe) for i in range(len(universe[0]))]
    j_offset = 0
    for j, line in enumerate(universe):
        if "#" not in line:
            j_offset += distance
            continue
        i_offset = 0
        for i, c in enumerate(line):
            if empty_columns[i]:
                i_offset += distance
                continue
            if c == "#":
                galaxies.append([j + j_offset, i + i_offset])
    total = 0
    for i, galaxy in enumerate(galaxies[:-1]):
        for other in galaxies[i + 1:]:
            total += abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
    return total


def read_input():
    values = []
    with open('input/day11.txt') as input_file:
        for line in input_file:
            values.append(line.rstrip())
    return values
