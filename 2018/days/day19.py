import days.day16 as functions
import math

def part1():
    """
    What value is left in register 0 when the background process halts?
    """
    ip_register, instructions = read_input()
    registers = [0]*6
    registers = execute_program(instructions, registers, ip_register)
    print(registers[0])


def part2():
    """
    This time, register 0 started with the value 1.
    What value is left in register 0 when this new background process halts?
    """
    # For this part, the input program needs to be reverse engineered.
    # The program calculates a value n, and then in O(n^2) calculates the sum of all divisors of n
    # For this input, with register 0 starting at value 1, n equals 10551347
    # Given the size of n the only feasible solution is to calculate the answer with a better algorithm
    ip_register, instructions = read_input()
    registers = [1] + [0] * 5

    pointer = registers[ip_register]
    # Execute program until n is calculated, then take over
    while pointer != 1:
        instruction = instructions[pointer]
        getattr(functions, instruction[0])(instruction[1], instruction[2], instruction[3], registers)
        registers[ip_register] += 1
        pointer = registers[ip_register]
    n = registers[4]
    # Calculate the sum of divisors efficiently
    sum_divisors = 0
    n_sqrt = int(math.sqrt(n))
    for i in range(1, n_sqrt+1):
        if n % i == 0:
            sum_divisors += i
            sum_divisors += int(n/i)
    print(sum_divisors)


def read_input():
    with open('input/day19.txt') as input_file:
        ip_register = int(input_file.readline()[-2])
        instructions = []
        for line in input_file:
            instructions.append([line[0:4]] + [int(n) for n in line[5:].split(' ')])
        return ip_register, instructions


def execute_program(instructions, registers, ip_register):
    pointer = registers[ip_register]
    while 0 <= pointer < len(instructions):
        instruction = instructions[pointer]
        getattr(functions, instruction[0])(instruction[1], instruction[2], instruction[3], registers)
        registers[ip_register] += 1
        pointer = registers[ip_register]
    return registers
