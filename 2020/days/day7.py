from collections import defaultdict


def part1():
    """
    Many rules (your puzzle input) are being enforced about bags and their contents;
    Bags must be color-coded and must contain specific quantities of other color-coded bags.
    How many bag colors can eventually contain at least one shiny gold bag?
    """
    # Bag rules is a dict with bag names as keys, and their required content as values.
    # The required content is a dict, with bag names as keys, and required amounts as values.
    bag_rules = read_input()
    # containers_of will have bag names as key, and a list of all possible bags directly containing that bag as values.
    containers_of = defaultdict(list)
    for container_name in bag_rules:
        for content_name in bag_rules[container_name]:
            containers_of[content_name].append(container_name)

    my_bag_name = "shiny gold"
    to_check = containers_of[my_bag_name]
    possible_containers = set(to_check)
    # Keep checking new container bags until all options have been exhausted
    while len(to_check):
        new_containers = set()
        for bag_type in to_check:
            new_containers = new_containers.union(set(containers_of[bag_type]))
        to_check = new_containers.difference(possible_containers)  # Next iteration, only check those bags we haven't checked before
        possible_containers = possible_containers.union(new_containers)  # Add the newly found containers to the set
    print(len(possible_containers))


def part2():
    """
    How many individual bags are required inside your single shiny gold bag?
    """
    bag_rules = read_input()
    my_bag_name = "shiny gold"
    amount_contained_by = dict()

    def get_amount(bag_name):
        if bag_name in amount_contained_by:
            return amount_contained_by[bag_name]
        this_amount = 0
        for content_name in bag_rules[bag_name]:
            content_amount = bag_rules[bag_name][content_name]
            this_amount += content_amount + content_amount*get_amount(content_name)
        amount_contained_by[bag_name] = this_amount
        return this_amount

    print(get_amount(my_bag_name))


def read_input():
    bag_rules = dict()
    with open('input/day7.txt') as input_file:
        # Example lines:
        # mirrored bronze bags contain 4 muted tomato bags, 4 bright white bags, 1 faded crimson bag.
        # wavy teal bags contain no other bags.
        for line in input_file:
            container_name, raw_contents = line.rstrip().split(' bags contain ')
            rule = dict()
            if raw_contents != "no other bags.":
                content_list = raw_contents.split(', ')
                for content in content_list:
                    parts = content.split(' ')
                    content_amount = int(parts[0])
                    content_color = ' '.join(parts[1:-1])
                    rule[content_color] = content_amount
            bag_rules[container_name] = rule
    return bag_rules
