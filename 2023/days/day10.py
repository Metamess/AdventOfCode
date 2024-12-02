def get_loop(start_position: tuple[int, int], maze: list[str]) -> list[tuple[int, int]]:
    """
    """
    j, i = start_position
    if j > 0 and maze[j - 1][i] in "|7F":
        j -= 1
    elif j < len(maze) and maze[j + 1][i] in "|JL":
        j += 1
    else:
        i += 1
    loop = [start_position, (j, i)]
    while (j, i) != start_position:
        pos = maze[j][i]

        # Try to go up
        if pos in "|JL" and loop[-2][0] >= j:
            # print(pos, "at", (j, i), "going up")
            j -= 1
        # Try to go down
        elif pos in "|7F" and loop[-2][0] <= j:
            # print(pos, "at", (j, i), "going down")
            j += 1
        # Try to go right
        elif pos in "-FL" and loop[-2][1] <= i:
            # print(pos, "at", (j, i), "going right")
            i += 1
        else:
            assert pos in "-J7" and loop[-1][1] >= i
            # print(pos, "at", (j, i), "going left")
            i -= 1
        loop.append((j, i))
    return loop[:-1]


def part1():
    """
    """
    return len(get_loop(*read_input())) // 2


def part2():
    """
    """
    start_position, maze = read_input()
    loop = get_loop(start_position, maze)

    extended_maze = []
    for line in maze:
        extended_maze.append(list("I " * len(line)))
        extended_maze.append(list("  " * len(line)))

    for pos1, pos2 in zip(loop, loop[1:] + loop[:1]):
        j, i = pos1
        m, n = pos2
        extended_maze[j*2][i*2] = "#"
        extended_maze[j + m][i + n] = "#"

    queue = ([(j, 0) for j in range(0, len(extended_maze), 2)] +
             [(j, len(extended_maze[j]) - 2) for j in range(0, len(extended_maze), 2)] +
             [(0, i) for i in range(0, len(extended_maze[0]), 2)] +
             [(len(extended_maze) - 2, i) for i in range(0, len(extended_maze[0]), 2)])

    while queue:
        j,  i = queue.pop()
        if extended_maze[j][i] in "O#":
            continue
        extended_maze[j][i] = "O"
        if i < len(extended_maze[j]) - 1 and extended_maze[j][i + 1] not in "O#":
            queue.append((j, i + 1))
        if i > 0 and extended_maze[j][i - 1] not in "O#":
            queue.append((j, i - 1))
        if j < len(extended_maze) - 1 and extended_maze[j + 1][i] not in "O#":
            queue.append((j + 1, i))
        if j > 0 and extended_maze[j - 1][i] not in "O#":
            queue.append((j - 1, i))

    return sum(line.count("I") for line in extended_maze)


def read_input():
    with open('input/day10.txt') as input_file:
        maze = input_file.read().split()
    start_position = (-1, -1)
    for j, line in enumerate(maze):
        start = line.find("S")
        if start >= 0:
            start_position = (j, start)
            break
    return start_position, maze
