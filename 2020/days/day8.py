
def part1():
    """
    The boot code is represented as a text file with one instruction per line of text.
    Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

    acc increases or decreases a single global value called the accumulator by the value given in the argument.
    jmp jumps to a new instruction relative to itself.
    nop stands for No OPeration - it does nothing.

    Run your copy of the boot code.
    Immediately before any instruction is executed a second time, what value is in the accumulator?
    """
    program = read_input()
    execution_count = [0]*len(program)
    instruction_pointer, accumulator = run_program(program, execution_count, 0, 0)
    print(accumulator)


def part2():
    """
    The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file.
    By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.
    What is the value of the accumulator after the program terminates?
    """
    program = read_input()
    execution_count = [0]*len(program)
    instruction_pointer = 0
    accumulator = 0
    target_pointer = len(program)
    # Run the program, but branch at every nop or jmp
    while True:
        if execution_count[instruction_pointer] != 0:
            print("Failed to find a solution")
            break
        operation, parameter = program[instruction_pointer]
        if operation == 'jmp':
            # First edit the program, and run a branch
            program[instruction_pointer][0] = "nop"
            result_pointer, result_acc = run_program(program, execution_count.copy(), instruction_pointer, accumulator)
            if result_pointer == target_pointer:
                print(result_acc)
                break
            # The branch was not the solution, carry on
            program[instruction_pointer][0] = "jmp"
            execution_count[instruction_pointer] += 1
            instruction_pointer += parameter
            continue
        elif operation == 'nop':
            # First edit the program, and run a branch
            program[instruction_pointer][0] = "jmp"
            result_pointer, result_acc = run_program(program, execution_count.copy(), instruction_pointer, accumulator)
            if result_pointer == target_pointer:
                print(result_acc)
                break
            # The branch was not the solution, carry on
            program[instruction_pointer][0] = "nop"
        elif operation == 'acc':
            accumulator += parameter
        execution_count[instruction_pointer] += 1
        instruction_pointer += 1


def run_program(program, execution_count, instruction_pointer, accumulator):
    while True:
        if instruction_pointer >= len(program):
            return instruction_pointer, accumulator
        if execution_count[instruction_pointer] != 0:
            return instruction_pointer, accumulator
        execution_count[instruction_pointer] += 1
        operation, parameter = program[instruction_pointer]
        if operation == 'jmp':
            instruction_pointer += parameter
            continue
        elif operation == 'acc':
            accumulator += parameter
        instruction_pointer += 1


def read_input():
    program = []
    with open('input/day8.txt') as input_file:
        for line in input_file:
            operation, parameter = line.split(' ')
            program.append([operation, int(parameter)])
    return program
