def part1():
    """
    The data consists of many reports, each report is a list of numbers called levels that are separated by spaces.
    Safe reports are either all strictly increasing or all strictly decreasing with no diff larger than 3.
    How many reports are safe?
    """
    reports = read_input()
    safe_count = 0
    for report in reports:
        diffs = [a - b for a, b in zip(report[:-1], report[1:])]
        if (min(diffs) >= 1 and max(diffs) <= 3) or (max(diffs) <= -1 and min(diffs) >= -3):
            safe_count += 1
    return safe_count


def part2():
    """
    How many reports are safe if you can skip a single value?
    """
    reports = read_input()
    safe_count = 0
    for report in reports:
        for i in range(len(report)):
            adjusted = report[:i] + report[i+1:]
            diffs = [a - b for a, b in zip(adjusted[:-1], adjusted[1:])]
            if (min(diffs) >= 1 and max(diffs) <= 3) or (max(diffs) <= -1 and min(diffs) >= -3):
                safe_count += 1
                break
    return safe_count


def read_input():
    values = []
    with open('input/day2.txt') as input_file:
        for line in input_file:
            values.append([int(a) for a in line.split()])
    return values
