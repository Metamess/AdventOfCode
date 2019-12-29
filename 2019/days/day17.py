from . import computer


def part1():
    """
    An Intcode program, (ASCII, your puzzle input), provides access to the cameras and the vacuum robot.
    Running the ASCII program on your Intcode computer will provide the current view of the scaffolds as ASCII code
    In the camera output, # represents a scaffold and . represents open space.
    The vacuum robot is visible as ^, v, <, or > depending on whether it is facing up, down, left, or right respectively.
    Locate all scaffold intersections; for each, its alignment parameter is the distance between its left edge
    and the left edge of the view multiplied by the distance between its top edge and the top edge of the view.
    What is the sum of the alignment parameters for the scaffold intersections?
    """
    program = read_input()
    output_values = []
    computer.run_program(program, [], output_values)
    scaffolding = ''.join(chr(c) for c in output_values).strip().split('\n')
    alignment_sum = 0
    for row in scaffolding:
        print(row)
    for j in range(1, len(scaffolding)-1):
        for i in range(1, len(scaffolding[0])-1):
            if scaffolding[j][i] == scaffolding[j-1][i] == scaffolding[j+1][i] == scaffolding[j][i-1] == scaffolding[j][i+1] == '#':
                alignment_sum += i*j
    print(alignment_sum)


def part2():
    """
    Force the vacuum robot to wake up by changing the value in your ASCII program at address 0 from 1 to 2.
    First, you will be prompted for the main movement routine. The main routine may only call the movement functions: A, B, or C.
    Supply the movement functions to use as ASCII text, separating them with commas (,, ASCII code 44), and ending the list with a newline (ASCII code 10).
    Then, you will be prompted for each movement function. Movement functions may use L to turn left, R to turn right, or a number to move forward that many units.
    Separate the actions with commas and end the list with a newline.
    Finally, you will be asked whether you want to see a continuous video feed; provide either y or n and a newline.
    The ASCII definitions of the main routine and the movement functions may each contain at most 20 characters, not counting the newline.
    Once it finishes the programmed set of movements, the robot will return a large value in a single output instruction.
    After visiting every part of the scaffold at least once, how much dust does the vacuum robot report it has collected?
    """
    # Solved manually:
    # L10 L10 R06 L10 L10 R06 R12 L12 L12 R12 L12 L12 L06 L10 R12 R12 R12 L12 L12 L06 L10 R12 R12 R12 L12 L12 L06 L10 R12 R12 L10 L10 R06
    #  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33
    # aaaaaaaaaaa aaaaaaaaaaa bbbbbbbbbbb bbbbbbbbbbb ccccccccccccccc bbbbbbbbbbb ccccccccccccccc bbbbbbbbbbb ccccccccccccccc aaaaaaaaaaa
    program = read_input()
    program[0] = 2
    input_values = "A,A,B,B,C,B,C,B,C,A\n"  # Main loop
    input_values += "L,10,L,10,R,6\n"  # Loop A
    input_values += "R,12,L,12,L,12\n"  # Loop B
    input_values += "L,6,L,10,R,12,R,12\n"  # Loop C
    input_values += "n\n"  # No further output
    input_values = [ord(c) for c in input_values]
    output_values = []
    computer.run_program(program, input_values, output_values)
    print(output_values[-1])


def read_input():
    with open('input/day17.txt') as input_file:
        return [int(x) for x in input_file.readline().split(',')]
