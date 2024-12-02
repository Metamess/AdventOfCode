def part1():
    """
    """
    return energize(read_input(), (0, 0, 0, 1))


def part2():
    """
    """
    grid = read_input()
    best_energy = 0
    for j in range(len(grid)):
        best_energy = max(best_energy, energize(grid, (j, 0, 0, 1)))
        best_energy = max(best_energy, energize(grid, (j, len(grid[0]), 0, -1)))
    for i in range(len(grid[0])):
        best_energy = max(best_energy, energize(grid, (0, i, 1, 0)))
        best_energy = max(best_energy, energize(grid, (len(grid), i, -1, 0)))
    return best_energy


def energize(grid: list[str], start_beam: tuple[int, int, int, int]) -> int:
    visited = {}
    beams = [start_beam]
    while beams:
        beam = beams.pop()
        while True:
            j, i, dy, dx = beam
            if j < 0 or i < 0 or j == len(grid) or i == len(grid[0]):
                break
            history = visited.setdefault((j, i), set())
            if (dy, dx) in history:  # or (-dy, dx) in history:
                break
            history.add((dy, dx))

            grid_char = grid[j][i]
            if grid_char == '\\':
                dy, dx = dx, dy
            elif grid_char == '/':
                dy, dx = -dx, -dy
            elif grid_char == '-' and dy:
                beams.extend([(j, i - 1, 0, -1), (j, i + 1, 0, 1)])
                break
            elif grid_char == '|' and dx:
                beams.extend([(j - 1, i, -1, 0), (j + 1, i, 1, 0)])
                break
            beam = (j + dy, i + dx, dy, dx)

    return len(visited)


def read_input() -> list[str]:
    with open('input/day16.txt') as input_file:
        return input_file.read().split('\n')
