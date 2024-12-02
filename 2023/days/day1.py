def part1():
    """
    """
    values = read_input()
    total = 0
    for line in values:
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


def part2():
    """
    """
    values = read_input()
    total = 0
    number_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in values:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
                continue
            for j, name in enumerate(number_names):
                if line[i:].startswith(name):
                    digits.append(str(j))
        # for i, number_name in enumerate(number_names):
        #     line = line.replace(number_name, number_name[0] + str(i) + number_name[-1])
        # digits = [c for c in line if c.isdigit()]
        line_res = int(digits[0] + digits[-1])
        total += line_res
    return total


def read_input():
    with open('input/day1.txt') as input_file:
        return input_file.read().split()
