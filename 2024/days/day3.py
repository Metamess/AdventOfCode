import re


def part1():
    """
    """
    lines = read_input()
    multiply_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    res = 0
    for line in lines:
        matches = multiply_pattern.findall(line)  # [('a', 'b'), ...]
        for a, b in matches:
            res += int(a) * int(b)
    return res


def part2():
    """
    """
    lines = read_input()
    full_pattern = re.compile(r"mul\((\d+),(\d+)\)|(do(?:n't)?)\(\)")
    res = 0
    enabled = True
    for line in lines:
        for a, b, instruction in full_pattern.findall(line):
            if instruction == "do":
                enabled = True
            elif instruction == "don't":
                enabled = False
            else:
                if enabled:
                    res += int(a) * int(b)
    return res


def read_input():
    values = []
    with open('input/day3.txt') as input_file:
        for line in input_file:
            values.append(line.rstrip())
    return values
