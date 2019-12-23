from . import computer


def add_tuples(a, b):
    return a[0] + b[0], a[1] + b[1]


def part1():
    """
    The remote control program executes the following steps in a loop forever:
    - Accept a movement command via an input instruction.
    - Send the movement command to the repair droid.
    - Wait for the repair droid to finish the movement operation.
    - Report on the status of the repair droid via an output instruction.
    Only four movement commands are understood: north (1), south (2), west (3), and east (4).
    The repair droid can reply with any of the following status codes:
    0: The repair droid hit a wall. Its position has not changed.
    1: The repair droid has moved one step in the requested direction.
    2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
    What is the fewest number of movement commands required to move the repair droid from its starting position to the location of the oxygen system?
    """
    program = read_input()
    input_values = []
    droid = computer.get_computer(program, input_values)
    room = dict()
    directions = [None, (0, -1), (0, 1), (-1, 0), (1, 0)]
    reverse = [None, 2, 1, 4, 3]
    position = (0, 0)
    distance = 0
    characters = ['#', ' ', 'O']
    came_from = [-1]
    iteration_state = [0]
    room[position] = (' ', distance)

    while True:
        while iteration_state[distance] < 4:
            iteration_state[distance] += 1
            i = iteration_state[distance]
            if i == came_from[distance]:
                continue
            input_values.append(i)
            result = next(droid)
            if result == 0:
                room[add_tuples(position, directions[i])] = (characters[result], distance + 1)
            else:
                next_position = add_tuples(position, directions[i])
                if next_position not in room or room[next_position][1] > distance + 1:
                    position = next_position
                    distance += 1
                    room[position] = (characters[result], distance)
                    came_from.append(reverse[i])
                    iteration_state.append(0)
                else:
                    input_values.append(reverse[i])
                    next(droid)
        if distance == 0:
            break
        input_values.append(came_from[distance])
        next(droid)
        position = add_tuples(position, directions[came_from[distance]])
        distance -= 1
        iteration_state.pop(-1)
        came_from.pop(-1)

    # min_x = min(k[0] for k in room.keys())
    # min_y = min(k[1] for k in room.keys())
    # max_x = max(k[0] for k in room.keys())
    # max_y = max(k[1] for k in room.keys())
    # visual = [['*'] * (1 + max_x - min_x) for _ in range(1 + max_y - min_y)]
    # for p in room:
    #     visual[abs(min_y) + p[1]][abs(min_x) + p[0]] = str(room[p][0])
    # for row in visual:
    #     print(''.join(row))

    for p in room:
        if room[p][0] == 'O':
            print(room[p][1])


def part2():
    """
    Oxygen starts in the location containing the repaired oxygen system.
    It takes one minute for oxygen to spread to all open locations that are adjacent to a location that already contains oxygen.
    How many minutes will it take to fill with oxygen?
    """
    program = read_input()
    input_values = []
    droid = computer.get_computer(program, input_values)
    room = dict()
    directions = [None, (0, -1), (0, 1), (-1, 0), (1, 0)]
    reverse = [None, 2, 1, 4, 3]
    position = (0, 0)
    distance = 0
    characters = ['#', ' ', 'O']
    came_from = [-1]
    iteration_state = [0]
    room[position] = (' ', distance)

    while True:
        while iteration_state[distance] < 4:
            iteration_state[distance] += 1
            i = iteration_state[distance]
            if i == came_from[distance]:
                continue
            input_values.append(i)
            result = next(droid)
            if result == 0:
                room[add_tuples(position, directions[i])] = (characters[result], distance + 1)
            else:
                next_position = add_tuples(position, directions[i])
                if next_position not in room or room[next_position][1] > distance + 1:
                    position = next_position
                    distance += 1
                    room[position] = (characters[result], distance)
                    came_from.append(reverse[i])
                    iteration_state.append(0)
                else:
                    input_values.append(reverse[i])
                    next(droid)
        if distance == 0:
            break
        input_values.append(came_from[distance])
        next(droid)
        position = add_tuples(position, directions[came_from[distance]])
        distance -= 1
        iteration_state.pop(-1)
        came_from.pop(-1)

    # Make new map for the oxygen, and start filling the room
    oxygen_map = dict()
    start = None
    for p in room:
        oxygen_map[p] = room[p][0]
        if room[p][0] == 'O':
            start = p
    time = 0
    current_minute = [start]
    while True:
        next_minute = []
        for position in current_minute:
            for direction in directions[1:]:
                next_position = add_tuples(position, direction)
                if oxygen_map[next_position] == ' ':
                    next_minute.append(next_position)
                    oxygen_map[next_position] = 'O'
        if not len(next_minute):
            break
        time += 1
        current_minute = next_minute
    print(time)


def read_input():
    with open('input/day15.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]
