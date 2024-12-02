def is_symbol(c: str) -> bool:
    if not c.isdigit() and c != ".":
        return True
    return False


def get_part_numbers(schematic: list[str]):
    """
    """
    part_numbers_by_row = {}
    for j, line in enumerate(schematic):
        number = ""
        is_part = False
        for i, c in enumerate(line):
            if c.isdigit():
                # Starting new number, check previous column
                if number == "":
                    is_part = any(is_symbol(schematic[j-k][i-1]) for k in [-1, 0, 1])
                number += c
                # Check up and down
                if not is_part:
                    is_part = is_symbol(schematic[j-1][i]) or is_symbol(schematic[j+1][i])
            else:
                # End of number
                if number != "":
                    if not is_part:
                        is_part = any(is_symbol(schematic[j-k][i]) for k in [-1, 0, 1])
                    # print(f"Found {'' if is_part else 'in'}valid number {number} ending at {j},{i}")
                    if is_part:
                        part_numbers_by_row.setdefault(j, {})[i-len(number)] = int(number)
                    number = ""
                    is_part = False
    return part_numbers_by_row


def part1():
    """
    """
    schematic: list[str] = read_input()
    total = 0
    for j, row_part_numbers in get_part_numbers(schematic).items():
        total += sum(int(num) for num in row_part_numbers.values())
    return total


def part2():
    """
    """
    schematic: list[str] = read_input()
    part_numbers_by_row = get_part_numbers(schematic)
    total = 0
    for j, line in enumerate(schematic):
        for i, c in enumerate(line):
            if c != "*":
                continue
            adjacent_numbers = []
            for row_nr in [j-1, j, j+1]:
                for number_i, number in part_numbers_by_row.get(row_nr, {}).items():
                    if number_i - 1 <= i <= number_i + len(str(number)):
                        adjacent_numbers.append(number)
                        # print(f"Gear at {j},{i} is adjacent to number {number} at {row_nr},{number_i}")
            if len(adjacent_numbers) == 2:
                total += adjacent_numbers[0] * adjacent_numbers[1]
    return total


def read_input():
    values = []
    with open('input/day3.txt') as input_file:
        for line in input_file:
            values.append("." + line.rstrip() + ".")
    filler_line = "." * len(values[0])
    return [filler_line] + values + [filler_line]
