from collections import Counter


def part1():
    """
    """
    return solve([Hand(cards, bid) for cards, bid in read_input()])


def part2():
    """
    """
    return solve([Hand(cards, bid, joker=True) for cards, bid in read_input()])


def solve(hands: list["Hand"]) -> int:
    return sum((i + 1) * hand.bid for i, hand in enumerate(sorted(hands)))


class Hand:
    def __init__(self, cards: str, bid: str, joker: bool = False):
        self.bid = int(bid)
        card_order = "J23456789TQKA" if joker else "23456789TJQKA"
        self.hand_value = [card_order.index(card) for card in cards]
        counter = Counter(cards)
        if joker and "J" in counter and len(counter) > 1:
            j_count = counter.pop("J")
            counter[counter.most_common()[0][0]] += j_count
        self.category = sorted(counter.values(), reverse=True)

    def __lt__(self, other: "Hand") -> bool:
        return (self.category, self.hand_value) < (other.category, other.hand_value)


def read_input():
    hands = []
    with open('input/day7.txt') as input_file:
        for line in input_file:
            hands.append([*line.split()])
    return hands
