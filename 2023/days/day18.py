def part1():
    """
    """
    return shoelace(read_input()[0])


def part2():
    """
    """
    return shoelace(read_input()[1])


def shoelace(instructions: list[tuple[str, int]]) -> int:
    x = y = 0
    points = [(0, 0)]
    perimeter = 0
    for direction, length in instructions:
        dy, dx = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[direction]
        y += dy * length
        x += dx * length
        perimeter += length
        points.append((x, y))

    area = 0
    for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
        area += x1 * y2 - x2 * y1

    return (area + perimeter + 2) // 2


# def solve(instructions: list[tuple[str, int]]) -> int:
#     # Make sure to start and end with the same vertical instruction
#     if instructions[0][0] in "RL":
#         instructions.insert(0, instructions[-1])
#     else:
#         instructions.append(instructions[0])
#
#     width_diffs: dict[int, list[int, int]] = {}
#     x = y = 0
#     delta = 0
#     for direction, length in instructions:
#         dy, dx = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[direction]
#         y_diff = width_diffs.setdefault(y, [0, 0])
#         if direction in "UD" and delta != 0:
#             delta += 0.5 if direction == "D" else -0.5
#             assert delta % 1 == 0
#             y_diff[0 if delta > 0 else 1] += int(delta)
#             delta = 0
#         elif direction == "R":
#             delta += length
#         elif direction == "L":
#             delta -= length
#         # Move
#         y += dy * length
#         x += dx * length
#         # Post-move actions for vertical instructions
#         if direction in "UD":
#             delta += 0.5 if direction == "U" else -0.5
#
#     total = 0
#     width = 0
#     prev_y = min(width_diffs)
#     for y, (pos_delta, neg_delta) in sorted(width_diffs.items()):
#         total += (y - prev_y) * width - neg_delta
#         width += pos_delta + neg_delta
#         prev_y = y
#
#     return total


def read_input():
    instruction_set_1 = []
    instruction_set_2 = []
    with open('input/day18.txt') as input_file:
        for line in input_file:
            dir1, len1, color = line.split()
            instruction_set_1.append((dir1, int(len1)))
            dir2 = ["R", "D", "L", "U"][int(color[-2])]
            len2 = int(color[2:7], base=16)
            instruction_set_2.append((dir2, len2))
    return instruction_set_1, instruction_set_2
