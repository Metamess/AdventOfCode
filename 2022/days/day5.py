import re


def part1():
    """
    Supplies are stored in stacks of marked crates, but the crates need to be rearranged.
    After the crates are rearranged, the desired crates will be at the top of each stack.
    They have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
    In each step of the procedure, a quantity of crates is moved from one stack to a different stack.
    Crates are moved one at a time, so the first crate to be moved ends up below the second.
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    stacks, procedure = read_input()
    for move, from_, to_ in procedure:
        stacks[to_] += stacks[from_][:-move-1:-1]
        stacks[from_] = stacks[from_][:-move]
    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


def part2():
    """
    The CrateMover 9001 has the ability to pick up and move multiple crates at once.
    That means that the moved crates stay in the same order.
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    stacks, procedure = read_input()
    for move, from_, to_ in procedure:
        stacks[to_] += stacks[from_][-move:]
        stacks[from_] = stacks[from_][:-move]
    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


def read_input():
    stacks = []
    procedure = []
    # move 6 from 9 to 3
    procedure_regex = re.compile('move (\d+) from (\d+) to (\d+)\n')
    with open('input/day5.txt') as input_file:
        while True:
            line = input_file.readline()
            if line[1] == '1':
                break
            while len(stacks) < len(line) // 4:
                stacks.append([])
            for i in range(len(line) // 4):
                crate = line[1 + 4*i]
                if crate != ' ':
                    stacks[i].append(crate)
        for stack in stacks:
            stack.reverse()
        # Done reading crate setup
        input_file.readline()
        # Start reading procedure
        for line in input_file:
            move, from_, to_ = map(int, re.match(procedure_regex, line).group(1, 2, 3))
            procedure.append((move, from_ - 1, to_ - 1))
    return stacks, procedure
