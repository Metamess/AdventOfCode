from queue import Queue


def part1():
    """
    """
    step_goal = 64
    grid = read_input()
    for j, line in enumerate(grid):
        if "S" in line:
            start = (j, line.index("S"))
            break
    else:
        raise ValueError("Couldn't find Start")

    distances = {}
    frontier = Queue()
    frontier.put((*start, 0))
    while not frontier.empty():
        j, i, d = frontier.get()
        if j < 0 or i < 0 or j >= len(grid) or i >= len(grid[0]) or d > step_goal:
            continue
        if (j, i) in distances:
            continue
        if grid[j][i] == "#":
            continue
        distances[(j, i)] = d
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            frontier.put((j + dy, i + dx, d + 1))

    return len([n for n in distances.values() if n % 2 == step_goal % 2])


def part2():
    """
    """
    step_goal = 26501365
    grid = read_input()
    for j, line in enumerate(grid):
        if "S" in line:
            start = (j, line.index("S"))
            break
    else:
        raise ValueError("Couldn't find Start")

    # step_goal = start[0] + 8 * len(grid)
    # print(f"Revised step goal: {step_goal}")

    assert grid[len(grid) // 2][len(grid[0]) // 2] == "S"
    assert start[0] == start[1]
    assert "#" not in grid[len(grid) // 2]
    assert "#" not in [grid[j][len(grid[0])//2] for j in range(len(grid))]

    grid_widths_to_step_goal = (step_goal - start[0]) // len(grid)
    assert (step_goal - start[0]) % len(grid) == 0
    steps_to_take = start[0] + 2 * len(grid)
    p0 = 0
    p1 = 0
    d1 = 0

    distances = {}
    frontier = Queue()
    frontier.put((*start, 0))
    while not frontier.empty():
        j, i, d = frontier.get()
        j_index = j % len(grid)
        i_index = i % len(grid[0])

        if p0 == 0 and d == start[0] + 1:
            p0 = len([n for n in distances.values() if n % 2 == step_goal % 2])
        if p1 == 0 and d == len(grid) + start[0] + 1:
            p1 = len([n for n in distances.values() if n % 2 == step_goal % 2])
            d1 = p1 - p0

        if d > steps_to_take:
            continue
        if (j, i) in distances:
            continue
        if grid[j_index][i_index] == "#":
            continue
        distances[(j, i)] = d
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            frontier.put((j + dy, i + dx, d + 1))

    p2 = len([n for n in distances.values() if n % 2 == step_goal % 2])
    d2 = (p2 - p1) // 2
    # print(p0, d1, d2)
    # for multiples in range(9):
    #     print([i * d1 if i % 2 == 1 else i * d2 for i in range(1, multiples + 1)])
    #     print(multiples, p0 + sum(i * d1 if i % 2 == 1 else i * d2 for i in range(1, multiples + 1)))

    return p0 + sum(i * d1 if i % 2 == 1 else i * d2 for i in range(1, grid_widths_to_step_goal + 1))


def read_input():
    with open('input/day21.txt') as input_file:
        return [list(line) for line in input_file.read().split()]
