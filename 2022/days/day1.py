def part1():
    """
    The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition
    traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies.
    One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input)

    The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
    that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's
    inventory (if any) by a blank line.

    In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many
    Calories are being carried by the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    """
    calories_per_elf = read_input()
    return max(sum(calories) for calories in calories_per_elf)


def part2():
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    """
    calories_per_elf = read_input()
    return sum(sorted(sum(calories) for calories in calories_per_elf)[-3:])


def read_input():
    values = [[]]
    with open('input/day1.txt') as input_file:
        for line in input_file:
            if not line.rstrip():
                values.append([])
            else:
                values[-1].append(int(line))
    return values
