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
    Memory address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.
    The arcade cabinet has a joystick that can move left and right.
    If the joystick is in the neutral position, provide 0.
    If the joystick is tilted to the left, provide -1.
    If the joystick is tilted to the right, provide 1.
    When three output instructions specify X=-1, Y=0, the third output instruction is the new score.
    What is your score after the last block is broken?
    """
    program = read_input()
    program[0] = 2
    input_values = []
    arcade = computer.get_computer(program, input_values)
    score = 0
    ball_x = 0
    paddle_x = 0
    while True:
        x = next(arcade)
        if type(x) == list:  # When the game is finished and the program halts, the computer outputs the program state
            break
        y = next(arcade)
        v = next(arcade)
        if v == 3:
            paddle_x = x
        elif v == 4:  # Every tick, the last value to be updated is that of the ball
            ball_x = x
            next_input = 0
            if ball_x < paddle_x:
                next_input = -1
            elif ball_x > paddle_x:
                next_input = 1
            input_values.append(next_input)
        if x == -1:
            score = v
    print(score)


def read_input():
    with open('input/day13.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]


class DefaultList(list):
    def __init__(self, constructor):
        self.constructor = constructor
        super(DefaultList, self).__init__()

    def __getitem__(self, item):
        if item >= len(self):
            self.extend([self.constructor() for _ in range(1+item-len(self))])
        return super(DefaultList, self).__getitem__(item)

    def __setitem__(self, key, value):
        if key >= len(self):
            self.extend([self.constructor() for _ in range(1+key-len(self))])
        return super(DefaultList, self).__setitem__(key, value)

    # legend = [' ', '|', '#', '_', 'O']
    # for row in display:
    #     print(''.join([legend[d] for d in row]))
