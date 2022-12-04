import re


def part1():
    """
    Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number,
    and each Elf is assigned a range of section IDs. They've noticed that many of the assignments overlap.
    To find overlaps the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).
    In how many assignment pairs does one range fully contain the other?
    """
    sections = read_input()
    res = 0
    for start1, end1, start2, end2 in sections:
        if start1 <= start2 and end1 >= end2 or start1 >= start2 and end1 <= end2:
            res += 1
    return res


def part2():
    """
    In how many assignment pairs do the ranges overlap?
    """
    sections = read_input()
    res = 0
    for start1, end1, start2, end2 in sections:
        if start1 <= end2 and end1 >= start2:
            res += 1
    return res


def read_input():
    values = []
    with open('input/day4.txt') as input_file:
        for line in input_file:
            values.append(map(int, re.split('[,-]', line.rstrip())))
    return values
