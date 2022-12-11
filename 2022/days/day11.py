import re
from math import prod


def part1():
    """
    Monkeys are playing Keep Away with your missing things!
    The monkeys operate based on how worried you are about each item.
    You take some notes (your puzzle input) on the items each monkey currently has,
    how worried you are about those items, and how the monkey makes decisions based on your worry level.

    Each monkey has several attributes:
    Starting items lists your worry level for each item the monkey is currently holding.
    Operation shows how your worry level changes as that monkey inspects an item.
    Test shows how the monkey uses your worry level to decide where to throw an item next.
        If true shows what happens with an item if the Test was true.
        If false shows what happens with an item if the Test was false.

    After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection
    didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.
    The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the
    items it is holding one at a time and in the order listed.
    The process of each monkey taking a single turn is called a round.

    Count the total number of times each monkey inspects items over 20 rounds.
    Focus on the two most active monkeys.
    The level of monkey business in this situation can be found by multiplying these together.
    What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
    """
    monkeys = read_input()
    for _ in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys, reduction=3)
    inspections = sorted([m.inspections for m in monkeys])
    return inspections[-1] * inspections[-2]


def part2():
    """
    Your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by 3.
    What is the level of monkey business after 10000 rounds?
    """
    monkeys = read_input()
    for _ in range(10000):
        for monkey in monkeys:
            cap = prod([m.test_int for m in monkeys])
            monkey.take_turn(monkeys, cap=cap)
    inspections = sorted([m.inspections for m in monkeys])
    return inspections[-1] * inspections[-2]


class Monkey:
    def __init__(self, number: int, starting_items: list[int], op_string: str, test_int: int, true_next: int, false_next: int):
        self.number = number
        self.item_list = starting_items
        operation_parts = op_string.split(' ')
        self.operation = ''.join(operation_parts[-3:])
        self.test_int = test_int
        self.next_if_true = true_next
        self.next_if_false = false_next
        self.inspections = 0

    def receive_item(self, item_number: int):
        self.item_list.append(item_number)

    def take_turn(self, monkey_list: list['Monkey'], reduction=1, cap=0):
        for old in self.item_list:
            self.inspections += 1
            new_ = eval(self.operation)
            new_ = new_ // reduction
            if cap:
                new_ = new_ % cap
            if new_ % self.test_int == 0:
                monkey_list[self.next_if_true].receive_item(new_)
            else:
                monkey_list[self.next_if_false].receive_item(new_)
        self.item_list = []


def read_input():
    """
    Monkey 0:
      Starting items: 71, 86
      Operation: new = old * 13
      Test: divisible by 19
        If true: throw to monkey 6
        If false: throw to monkey 7

    """
    values = []
    with open('input/day11.txt') as input_file:
        while True:
            monkey_input = [input_file.readline().strip() for _ in range(7)]
            if not monkey_input[0]:
                break
            number = int(re.search(r"\d+", monkey_input[0])[0])
            items = [int(d) for d in re.findall(r"\d+", monkey_input[1])]
            operation = re.search("= (.*)", monkey_input[2])[1]
            test_int = int(re.search(r"\d+", monkey_input[3])[0])
            true_next = int(re.search(r"\d+", monkey_input[4])[0])
            false_next = int(re.search(r"\d+", monkey_input[5])[0])
            values.append(Monkey(number, items, operation, test_int, true_next, false_next))
    return values
