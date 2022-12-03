from functools import reduce


def part1():
    """
    Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two.
    The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
    The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your
    help finding the errors. Every item type is identified by a single lowercase or uppercase letter
    (that is, a and A refer to different types of items).
    The list of items for each rucksack is given as characters all on a single line.
    A given rucksack always has the same number of items in each of its two compartments, so the first half of the
    characters represent items in the first compartment, while the second half of the characters represent items in the
    second compartment.
    To help prioritize item rearrangement, every item type can be converted to a priority:
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """
    rucksacks = read_input()
    total = 0
    for contents in rucksacks:
        half = len(contents) // 2
        duplicate = (set(contents[:half]) & set(contents[half:])).pop()
        if duplicate.isupper():
            total += ord(duplicate) - ord('A') + 27
        else:
            total += ord(duplicate) - ord('a') + 1
    return total


def part2():
    """
    For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group.
    For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
    Find the item type that corresponds to the badges of each three-Elf group.
    What is the sum of the priorities of those item types?
    """
    rucksacks = read_input()
    total = 0
    for i in range(0, len(rucksacks), 3):
        badge = reduce(set.intersection, map(set, rucksacks[i:i+3])).pop()
        if badge.isupper():
            total += ord(badge) - ord('A') + 27
        else:
            total += ord(badge) - ord('a') + 1
    return total


def read_input():
    values = []
    with open('input/day3.txt') as input_file:
        for line in input_file:
            values.append(line.rstrip())
    return values
