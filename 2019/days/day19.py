from . import computer


def part1():
    """
    The program uses two input instructions to request the X and Y position to which the drone should be deployed.
    Then, the program will output whether the drone is stationary (0) or being pulled by something (1)
    How many points are affected by the tractor beam in the 50x50 area closest to the emitter?
    """
    program = read_input()
    res = 0
    for x in range(50):
        for y in range(50):
            output_values = []
            computer.run_program(program, [x, y], output_values)
            res += output_values[0]
    print(res)


def part2():
    """
    Find the 100x100 square closest to the emitter that fits entirely within the tractor beam; within that square, find the point closest to the emitter.
    What value do you get if you take that point's X coordinate, multiply it by 10000, then add the point's Y coordinate?
    """
    program = read_input()

    def in_beam(x_pos, y_pos):
        return next(computer.get_computer(program, [x_pos, y_pos]))

    def descend(from_x, from_y):
        next_y = from_y + 1
        next_x = from_x
        while in_beam(next_x - 1, next_y):
            next_x -= 1
        while not in_beam(next_x, next_y):
            next_x += 1
        return next_x, next_y

    def get_diagonal(lower_x, lower_y, min_diagonal=1):
        while in_beam(lower_x + min_diagonal, lower_y - min_diagonal):
            min_diagonal += 1
        return min_diagonal

    target = 100
    y = target
    x = 0
    # find the lower x of the beam
    x, y = descend(x, y)
    diagonal = get_diagonal(x, y)
    while True:
        x, y = descend(x, y)
        new_diagonal = get_diagonal(x, y, diagonal)
        if new_diagonal > diagonal:
            diagonal = new_diagonal
            break
    factor = target//diagonal
    x *= factor
    y *= factor
    while diagonal < target:
        x, y = descend(x, y)
        diagonal = get_diagonal(x, y, diagonal)
    print(x * 10000 + y - (target - 1))


def read_input():
    with open('input/day19.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]
