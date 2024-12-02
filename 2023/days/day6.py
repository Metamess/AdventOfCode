import math


def part1():
    """
    """
    times, records = read_input()
    winning_option_amount = []
    for t, r in zip(times, records):
        d = math.sqrt(t*t - (4 * -1 * -(r+1)))
        first_win = math.ceil((-t + d)/-2)
        winners = t + 1 - 2 * first_win
        winning_option_amount.append(winners)
    return math.prod(winning_option_amount)


def part2():
    """
    """
    times, records = read_input()
    t = int(''.join(str(t) for t in times))
    r = int(''.join(str(r) for r in records))
    d = math.sqrt(t * t - (4 * -1 * -(r + 1)))
    first_win = math.ceil((-t + d) / -2)
    winners = t + 1 - 2 * first_win
    return winners


def read_input():
    with open('input/day6.txt') as input_file:
        times = [int(t) for t in input_file.readline().split()[1:]]
        records = [int(r) for r in input_file.readline().split()[1:]]
    return times, records
