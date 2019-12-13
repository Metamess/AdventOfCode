from . import computer


def part1():
    """
    The BOOST program will ask for a single input; run it in test mode by providing it the value 1.
    It should only output a single value, the BOOST keycode.
    What BOOST keycode does it produce?
    """
    program = read_input()
    output = []
    computer.run_program(program, [1], output)
    assert len(output) == 1
    print(output[0])


def part2():
    """
    The program runs in sensor boost mode by providing the input instruction the value 2.
    In sensor boost mode, the program will output a single value: the coordinates of the distress signal.
    What are the coordinates of the distress signal?
    """
    program = read_input()
    output = []
    computer.run_program(program, [2], output)
    assert len(output) == 1
    print(output[0])


def read_input():
    with open('input/day9.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]
