def part1():
    """
    """
    return solve(smudges=0)


def part2():
    """
    """
    return solve(smudges=1)


def solve(smudges: int):
    patterns = read_input()
    total = 0
    for pattern in patterns:
        # Try to find vertical reflection
        reflection_point = 100 * find_smudged_reflection_point(pattern, smudges)
        if not reflection_point:
            # Rotate pattern and try horizontal reflection
            pattern = [''.join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]
            reflection_point = find_smudged_reflection_point(pattern, smudges)

        total += reflection_point
    return total


def find_smudged_reflection_point(pattern, smudges=0, inverted=False):
    for i in range(1, len(pattern)//2 + 1):
        inverse = pattern[2*i - 1:i - 1:-1]
        matches = [a == b for a, b in zip(''.join(pattern[:i]), ''.join(inverse))]
        if matches.count(False) == smudges:
            if inverted:
                return len(pattern) - i
            return i
    if inverted:
        # "No match found"
        return 0
    # "Trying inverse"
    return find_smudged_reflection_point(list(reversed(pattern)), smudges, True)


def read_input():
    with open('input/day13.txt') as input_file:
        patterns = [pattern.split() for pattern in input_file.read().split("\n\n")]
    return patterns
