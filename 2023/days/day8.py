from functools import reduce


def part1():
    """
    """
    instructions, nodes_map = read_input()
    step_count = 0
    node = "AAA"
    while node != "ZZZ":
        left, right = nodes_map[node]
        if instructions[step_count % len(instructions)] == "L":
            node = left
        else:
            node = right
        step_count += 1
    return step_count


def part2():
    """
    """
    instructions, nodes_map = read_input()
    steps_per_node = []
    nodes = [node for node in nodes_map.keys() if node.endswith("A")]
    for node in nodes:
        step_count = 0
        while not node.endswith("Z"):
            left, right = nodes_map[node]
            if instructions[step_count % len(instructions)] == "L":
                node = left
            else:
                node = right
            step_count += 1
        steps_per_node.append(step_count)

    return reduce(lcm, steps_per_node)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def read_input():
    with open('input/day8.txt') as input_file:
        instructions, nodes_input = input_file.read().split("\n\n")
        nodes = {line[:3]: (line[7:10], line[12:15]) for line in nodes_input.split("\n")}
    return instructions, nodes
