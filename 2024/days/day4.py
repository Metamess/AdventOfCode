def part1():
    """
    """
    puzzle = read_input()
    max_y = len(puzzle) - 1
    max_x = len(puzzle[0]) - 1
    word_count = 0
    for y, line in enumerate(puzzle):
        for x, _ in enumerate(line):
            for y_dir in [-1, 0, 1]:
                if y_dir == -1 and y - 3 < 0:
                    continue
                if y_dir == 1 and y + 3 > max_y:
                    continue
                for x_dir in [-1, 0, 1]:
                    if y_dir == 0 and x_dir == 0:
                        continue
                    if x_dir == -1 and x - 3 < 0:
                        continue
                    if x_dir == 1 and x + 3 > max_x:
                        continue
                    word = ''.join([puzzle[y + i * y_dir][x + i * x_dir] for i in range(4)])
                    if word == "XMAS":
                        word_count += 1
    return word_count


def part2():
    """
    """
    puzzle = read_input()
    word_count = 0
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if x == 0 or x == len(line) - 1 or y == 0 or y == len(puzzle) - 1:
                continue
            if char != "A":
                continue
            if puzzle[y-1][x-1] + puzzle[y+1][x+1] in ["MS", "SM"] and puzzle[y+1][x-1] + puzzle[y-1][x+1] in ["MS", "SM"]:
                word_count += 1
    return word_count


def read_input():
    values = []
    with open('input/day4.txt') as input_file:
        for line in input_file:
            values.append(line.rstrip())
    return values
