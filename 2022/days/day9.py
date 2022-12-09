
def part1():
    """
    Consider a rope with a knot at each end; these knots mark the head and the tail of the rope.
    If the head moves far enough away from the tail, the tail is pulled toward the head.
    You should be able to model the positions of the knots on a two-dimensional grid.
    Then, by following a series of motions (your puzzle input) for the head, you can determine how the tail will move.
    The head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching).
    If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in
    that direction so it remains close enough. Otherwise, if the head and tail aren't touching and aren't in the same
    row or column, the tail always moves one step diagonally to keep up.
    You just need to work out where the tail goes as the head follows a series of motions.
    Assume the head and the tail both start at the same position, overlapping.
    How many positions does the tail of the rope visit at least once?
    """
    movements = read_input()
    return get_tail_location_count(movements, 1)


def part2():
    """
    Rather than two knots, you now must simulate a rope consisting of ten knots.
    One knot is still the head of the rope and moves according to the series of motions.
    Each knot further down the rope follows the knot in front of it using the same rules as before.
    How many positions does the tail of the rope visit at least once?
    """
    movements = read_input()
    return get_tail_location_count(movements, 9)


def get_tail_location_count(movements: list[tuple[str, int]], nr_of_tails: int) -> int:
    visited_locations: dict[int, list[int]] = {0: [0]}
    knots = [[0, 0] for _ in range(nr_of_tails + 1)]
    moves = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    for direction, steps in movements:
        for _ in range(steps):
            for i in range(len(knots)):
                knot = knots[i]
                knot_moved = False
                if i == 0:
                    # Determine movement for the head
                    diff = moves[direction]
                    knot_moved = True
                else:
                    head = knots[i-1]
                    # Determine movement for the tail
                    diff = [h - k for h, k in zip(head, knot)]
                    for axis in range(len(diff)):
                        if abs(diff[axis]) > 1:
                            knot_moved = True
                            # Move one less than the diff to become adjacent
                            diff[axis] += 1 if diff[axis] < 0 else -1
                if knot_moved:
                    knot = [k + d for k, d in zip(knot, diff)]
                    if i == nr_of_tails:
                        visited_locations.setdefault(knot[0], []).append(knot[1])
                    knots[i] = knot
    return sum(len(set(locations)) for locations in visited_locations.values())


def read_input():
    values = []
    with open('input/day9.txt') as input_file:
        for line in input_file:
            direction, steps = line.rstrip().split(' ')
            values.append((direction, int(steps)))
    return values
