
def part1():
    """
    The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values.
    - Action N means to move north by the given value.
    - Action S means to move south by the given value.
    - Action E means to move east by the given value.
    - Action W means to move west by the given value.
    - Action L means to turn left the given number of degrees.
    - Action R means to turn right the given number of degrees.
    - Action F means to move forward by the given value in the direction the ship is currently facing.
    The ship starts by facing east.
    Figure out where the navigation instructions lead.
    What is the Manhattan distance between that location and the ship's starting position?
    """
    instruction_list = read_input()
    ship_x, ship_y = 0, 0
    headings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ship_heading = 0
    for action, amount in instruction_list:
        if action == 'N':
            ship_y += amount
        elif action == 'S':
            ship_y -= amount
        elif action == 'E':
            ship_x += amount
        elif action == 'W':
            ship_x -= amount
        elif action == 'L':
            ship_heading = (ship_heading + (amount // 90)) % 4
        elif action == 'R':
            ship_heading = (ship_heading - (amount // 90)) % 4
        elif action == 'F':
            ship_x += headings[ship_heading][0] * amount
            ship_y += headings[ship_heading][1] * amount
    print(abs(ship_y) + abs(ship_x))


def part2():
    """
    Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
    - Action N means to move the waypoint north by the given value.
    - Action S means to move the waypoint south by the given value.
    - Action E means to move the waypoint east by the given value.
    - Action W means to move the waypoint west by the given value.
    - Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    - Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    - Action F means to move forward to the waypoint a number of times equal to the given value.
    The waypoint starts 10 units east and 1 unit north relative to the ship.
    The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
    Figure out where the navigation instructions actually lead.
    What is the Manhattan distance between that location and the ship's starting position?
    """
    instruction_list = read_input()
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    for action, amount in instruction_list:
        if action == 'N':
            waypoint_y += amount
        elif action == 'S':
            waypoint_y -= amount
        elif action == 'E':
            waypoint_x += amount
        elif action == 'W':
            waypoint_x -= amount
        elif action == 'L':
            for _ in range(amount // 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif action == 'R':
            for _ in range(amount // 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'F':
            ship_x += waypoint_x * amount
            ship_y += waypoint_y * amount
    print(abs(ship_y) + abs(ship_x))


def read_input():
    instruction_list = []
    with open('input/day12.txt') as input_file:
        for line in input_file:
            instruction_list.append((line[0], int(line.rstrip()[1:])))
    return instruction_list
