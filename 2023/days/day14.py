def part1():
    """
    """
    platform = read_input()
    total = 0
    for j in range(len(platform[0])):
        cube_pos = -1
        rock_count = 0
        for i in range(len(platform)):
            if platform[i][j] == "O":
                rock_count += 1
            elif platform[i][j] == "#":
                total += sum(range(len(platform) - cube_pos - 1, len(platform) - cube_pos - 1 - rock_count, -1))
                rock_count = 0
                cube_pos = i
        total += sum(range(len(platform) - cube_pos - 1, len(platform) - cube_pos - 1 - rock_count, -1))

    return total


def part2():
    """
    """
    _TOTAL_ITERATIONS = 1000000000
    platform = read_input()
    history = {}
    platform_str = ''
    iteration = 0
    for iteration in range(_TOTAL_ITERATIONS):
        platform_str = ''.join(''.join(row) for row in platform)
        if platform_str in history:
            break
        history[platform_str] = iteration
        # Tilt and rotate 4 times
        platform = tilt_and_rotate(tilt_and_rotate(tilt_and_rotate(tilt_and_rotate(platform))))

    cycle_start = history[platform_str]

    cycle_size = iteration - cycle_start
    remainder = (_TOTAL_ITERATIONS - cycle_start) % cycle_size
    final = list(history.keys())[cycle_start + remainder]
    final_platform = [list(final[i: i + len(platform[0])]) for i in range(0, len(final), len(platform[0]))]

    return sum(row.count("O") * (len(platform) - i) for i, row in enumerate(final_platform))


def tilt_and_rotate(platform: list[list[str]]) -> list[list[str]]:
    new_platform = []
    for i in range(len(platform[0])):
        section_start = len(platform)
        rock_count = 0
        new_row = []
        for j in reversed(range(len(platform))):
            char = platform[j][i]
            if char == ".":
                continue
            if char == "O":
                rock_count += 1
                continue
            # char == #
            empty_length = section_start - (j + 1) - rock_count
            new_row.extend(["."] * empty_length)
            new_row.extend(["O"] * rock_count)
            new_row.append("#")
            section_start = j
            rock_count = 0
        empty_length = section_start - rock_count
        new_row.extend(["."] * empty_length)
        new_row.extend(["O"] * rock_count)
        assert len(new_row) == len(platform)
        new_platform.append(new_row)

    return new_platform


def read_input():
    values = []
    with open('input/day14.txt') as input_file:
        for line in input_file:
            values.append(list(line.rstrip()))
    return values
