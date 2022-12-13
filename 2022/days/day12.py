
def part1():
    """
    A heightmap of the surrounding area is your puzzle input.
    Each square of the grid is given by a single lowercase letter, where a is the lowest elevation,
    b is the next-lowest, and so on up to the highest elevation, z.
    On the heightmap are marks for your current position (S) and the location that should get the best signal (E).
    Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.
    You'd like to reach E, but to save energy, you should do it in as few steps as possible.
    During each step, you can move exactly one square up, down, left, or right.
    The elevation of the destination square can be at most one higher than the elevation of your current square.
    The elevation of the destination square can be much lower than the elevation of your current square.
    What is the fewest steps required to move from your current position to the (E)?
    """
    heightmap: list[list[str]] = read_input()
    start = (0, 0)
    for i in range(len(heightmap)):
        try:
            s = heightmap[i].index("S")
        except ValueError:
            continue
        start = (i, s)
        break
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    symbols = ["^", "V", "<", ">", "S", "E"]
    current_positions = [(start, 'a')]
    steps = 0
    finish = False
    while not finish:
        steps += 1
        new_positions = []
        for pos, current_height in current_positions:
            for i, d in enumerate(directions):
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(heightmap) or new_pos[1] >= len(heightmap[0]):
                    continue
                new_height = heightmap[new_pos[0]][new_pos[1]]
                if new_height == "E" and ord(current_height) >= ord('z') - 1:
                    finish = True
                    break
                if new_height not in symbols and ord(new_height) - ord(current_height) < 2:
                    heightmap[new_pos[0]][new_pos[1]] = symbols[i]
                    new_positions.append((new_pos, new_height))
        current_positions = new_positions
    return steps


def part2():
    """
    What is the fewest steps required to move starting from any square with elevation a to (E)?
    """
    heightmap: list[list[str]] = read_input()
    start = (0, 0)
    for i in range(len(heightmap)):
        try:
            s = heightmap[i].index("E")
        except ValueError:
            continue
        start = (i, s)
        break
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    symbols = ["^", "V", "<", ">", "S", "E"]
    current_positions = [(start, 'z')]
    steps = 0
    finish = False
    while not finish:
        steps += 1
        new_positions = []
        for pos, current_height in current_positions:
            for i, d in enumerate(directions):
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(heightmap) or new_pos[1] >= len(heightmap[0]):
                    continue
                new_height = heightmap[new_pos[0]][new_pos[1]]
                if (new_height == "a" or new_height == "S") and current_height == 'b':
                    finish = True
                    break
                if new_height not in symbols and ord(current_height) - 1 <= ord(new_height):
                    heightmap[new_pos[0]][new_pos[1]] = symbols[i]
                    new_tuple = (new_pos, new_height)
                    new_positions.append(new_tuple)
        current_positions = new_positions
    return steps


def read_input():
    values = []
    with open('input/day12.txt') as input_file:
        for line in input_file:
            values.append(list(line.rstrip()))
    return values
