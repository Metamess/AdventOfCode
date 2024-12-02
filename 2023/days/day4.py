def part1():
    """
    """
    values = read_input()
    total = 0
    for winners, numbers in values:
        intersection = set(winners).intersection(numbers)
        if intersection:
            total += 2 ** (len(intersection) - 1)
    return total


def part2():
    """
    """
    values = read_input()
    copy_count = {i: 1 for i in range(len(values))}
    for i, (winners, numbers) in enumerate(values):
        intersection = set(winners).intersection(numbers)
        if intersection:
            for j in range(i + 1, i + len(intersection) + 1):
                copy_count[j] += copy_count[i]
    return sum(copy_count.values())


def read_input():
    values = []
    with open('input/day4.txt') as input_file:
        for line in input_file:
            _, info = line.rstrip().split(": ")
            winners, numbers = ([int(c) for c in part.split()] for part in info.split(" | "))
            values.append((winners, numbers))
    return values
