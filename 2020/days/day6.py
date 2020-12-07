from functools import reduce


def part1():
    """
    The form asks a series of 26 yes-or-no questions marked a through z.
    You need to identify the questions for which anyone in a group answers "yes".
    For each of the people in a group, you write down the questions for which they answer "yes", one per line.
    For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
    """
    group_answers = read_input()
    total = 0
    for group in group_answers:
        total += len(reduce(lambda x, y: x.union(y), [set(answers) for answers in group]))
    print(total)


def part2():
    """
    For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
    """
    group_answers = read_input()
    total = 0
    for group in group_answers:
        total += len(reduce(lambda x, y: x.intersection(y), [set(answers) for answers in group]))
    print(total)


def read_input():
    group_answers = [[]]
    with open('input/day6.txt') as input_file:
        for line in input_file:
            if line == '\n':
                group_answers.append([])
                continue
            group_answers[-1].append(line.rstrip())
    return group_answers
