def part1():
    """
    """
    metrics = read_input()
    total = 0
    for history in metrics:
        diffs = [history]
        while any(diffs[-1]):
            diffs.append(list(b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])))
        total += sum(diff[-1] for diff in diffs)
    return total


def part2():
    """
    """
    metrics = read_input()
    total = 0
    for history in metrics:
        diffs = [history]
        while any(diffs[-1]):
            diffs.append(list(a - b for a, b in zip(diffs[-1][:-1], diffs[-1][1:])))
        total += sum(diff[0] for diff in diffs)
    return total


def read_input():
    values = []
    with open('input/day9.txt') as input_file:
        for line in input_file:
            values.append([int(i) for i in line.split()])
    return values
