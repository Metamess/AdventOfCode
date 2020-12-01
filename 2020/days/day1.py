
def part1():
    """
    Find the two entries that sum to 2020 and then multiply those two numbers together.
    """
    values = read_input()
    values.sort()
    target = 2020
    i, j = 0, len(values)-1

    while True:
        total = values[i] + values[j]
        if total == target:
            break
        if total < target:
            i += 1
        else:
            j -= 1
    print(values[i]*values[j])


def part2():
    """
    Find three numbers in your expense report that meet the same criteria.
    What is the product of the three entries that sum to 2020?
    """
    values = read_input()
    values.sort()
    target = 2020
    k = 0
    while True:
        i, j = k + 1, len(values) - 1
        while True:
            total = values[k] + values[i] + values[j]
            if total == target or i == j:
                break
            if total < target:
                i += 1
            else:
                j -= 1
        if total == target:
            break
        k += 1

    print(values[i] * values[j] * values[k])


def read_input():
    values = []
    with open('input/day1.txt') as input_file:
        for line in input_file:
            values.append(int(line))
    return values
