
def part1():
    """
    The device's video system is a screen and simple CPU that are both driven by a precise clock circuit.
    The clock circuit ticks at a constant rate; each tick is called a cycle.
    The CPU has a single register, X, which starts with the value 1. It supports only two instructions:
      'addx V' takes two cycles to complete, after which the X register is increased by the value V (V can be negative).
      'noop' takes one cycle to complete. It has no other effect.
    The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.
    The signal strength is the cycle number multiplied by the value of the X register.
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    What is the sum of these six signal strengths?
    """
    program = read_input()
    execution = run_program(program, 220)
    strength = 0
    for cycle, register in execution:
        if (cycle + 21) % 40 == 0:
            strength += (cycle + 1) * register
    return strength


def part2():
    """
    The X register controls the horizontal position of a sprite which is 3 pixels wide.
    The X register sets the horizontal position of the middle of that sprite.
    There is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is
    currently drawing, then those pixels will be drawn. The pixels on the CRT: 40 wide and 6 high.
    This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on.
    The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.
    Render the image given by your program. What eight capital letters appear on your CRT?
    """
    program = read_input()
    execution = run_program(program, 240)
    output = [[] for _ in range(6)]
    for cycle, register in execution:
        if abs((cycle % 40) - register) <= 1:
            symbol = '#'
        else:
            symbol = ' '
        output[cycle // 40].append(symbol)
    return '\n'.join(''.join(line) for line in output)


def run_program(program, max_cycle):
    # General idea:
    # Execution of operations 'lags' behind the clock cycle, initially by 1 tick
    # 'noop' causes the op_id to be incremented, keeping the lag the same
    # 'addx' changes the register but does not increment the op_id, increasing the lag by 1
    # after execution, 'addx' changes into 'noop' to cause the next cycle to increment the op_id again
    op_id = -1
    register = 1
    op = ["noop"]
    for cycle in range(max_cycle):
        yield cycle, register
        if op[0] == "noop":
            op_id += 1
            op = program[op_id]
        else:
            register += op[1]
            op = ["noop"]


def read_input():
    values = []
    with open('input/day10.txt') as input_file:
        for line in input_file:
            op = [line[:4]]
            if len(line) > 5:
                op.append(int(line[5:-1]))
            values.append(op)
    return values
