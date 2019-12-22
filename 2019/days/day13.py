from . import computer


def part1():
    """
    The software draws tiles to the screen with output instructions:
    every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id.

    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.

    How many block tiles are on the screen when the game exits?
    """
    program = read_input()
    output_values = []
    computer.run_program(program, [], output_values)
    blocks = output_values[2::3].count(2)
    print(blocks)


def part2():
    """

    """
    pass


def read_input():
    with open('input/day13.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]
