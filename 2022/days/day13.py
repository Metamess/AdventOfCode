
def part1():
    """
    Your puzzle input consists of pairs of packets; pairs are separated by a blank line.
    You need to identify how many pairs of packets are in the right order.
    Packet data consists of lists and integers.
    When comparing two values, the first value is called left and the second value is called right. Then:
    - If both values are integers, the lower integer should come first.
      If the left integer is lower than the right integer, the inputs are in the right order.
      If the left integer is higher than the right integer, the inputs are not in the right order.
      Otherwise, the inputs are the same integer; continue checking the next part of the input.
    - If both values are lists, compare the first value of each list, then the second value, and so on.
      If the left list runs out of items first, the inputs are in the right order.
      If the right list runs out of items first, the inputs are not in the right order.
      If the lists are the same length and no comparison makes a decision about the order, continue checking.
    - If exactly one value is an integer, convert the integer to a list, then retry the comparison.
    Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
    """
    pairs = zip(*[iter(read_input())]*2)
    result = 0
    for i, (first, second) in enumerate(pairs):
        if Packet(first) < Packet(second):
            result += i + 1
    return result


def part2():
    """
    The distress signal protocol also requires that you include two additional divider packets: [[2]] and [[6]].
    The decoder key for this distress signal is the indices of the two divider packets multiplied together.
    Organize all of the packets into the correct order. What is the decoder key for the distress signal?
    """
    packet_contents = read_input()
    divider_1 = Packet([[2]])
    divider_2 = Packet([[6]])
    packets = [Packet(content) for content in packet_contents] + [divider_1, divider_2]
    packets.sort()
    return (packets.index(divider_1) + 1) * (packets.index(divider_2) + 1)


class Packet:
    def __init__(self, content):
        self.content = content

    @staticmethod
    def is_ordered(list1, list2) -> int:
        for item1, item2 in zip(list1, list2):
            if isinstance(item1, int):
                if isinstance(item2, int):
                    if item1 < item2:
                        return 1
                    if item2 < item1:
                        return -1
                    continue
                else:
                    item1 = [item1]
            elif isinstance(item2, int):
                item2 = [item2]
            result = Packet.is_ordered(item1, item2)
            if result != 0:
                return result
        if len(list1) < len(list2):
            return 1
        if len(list2) < len(list1):
            return -1
        return 0

    def __lt__(self, other):
        return self.is_ordered(self.content, other.content) == 1


def read_input():
    values = []
    with open('input/day13.txt') as input_file:
        while True:
            line = input_file.readline().rstrip()
            if not line:
                break
            values.append(eval(line))
            values.append(eval(input_file.readline()))
            input_file.readline()
    return values
