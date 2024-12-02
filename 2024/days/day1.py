from collections import Counter


def part1():
    """
    Pair up the numbers in the two lists from smallest to largest and calculate the total pair-wise difference.
    """
    list_a, list_b = read_input()
    res = 0
    for a, b in zip(sorted(list_a), sorted(list_b)):
        res += abs(a-b)
    return res


def part2():
    """
    Calculate a total similarity score by adding up each number in the left list after multiplying it by
    the number of times that number appears in the right list.
    """
    list_a, list_b = read_input()
    counter_a = Counter(list_a)
    counter_b = Counter(list_b)
    res = 0
    for a, a_count in counter_a.items():
        res += a_count * a * counter_b[a]
    return res


def read_input():
    list_a = []
    list_b = []
    with open('input/day1.txt') as input_file:
        for line in input_file:
            a, b = line.split()
            list_a.append(int(a))
            list_b.append(int(b))
    return list_a, list_b
