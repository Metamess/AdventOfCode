def part1():
    """
    """
    return solve(1)


def part2():
    """
    """
    return solve(5)


def solve(factor: int):
    values = read_input(factor)

    total = 0
    sub_solutions = {}
    for field, sequence in values:
        res = solve_partial(field, sequence, sub_solutions)
        total += res

    return total


def solve_partial(field: str, given_sequence: tuple[int, ...], sub_solutions: dict[(str, tuple[int]), int]):
    if (field, given_sequence) in sub_solutions:
        return sub_solutions[(field, given_sequence)]
    res = 0
    consuming = False
    sequence = list(given_sequence)
    for i, c in enumerate(field):
        if len(sequence) == 0:
            if "#" in field[i:]:
                # Consumed all sequences but hardcoded '#' left
                res = 0
                break
            else:
                # Valid mutation found!
                res = 1
                break

        if consuming:
            if sequence[0] == 0:
                if c == "#":
                    # Done consuming but character is a spring
                    res = 0
                    break
                else:
                    # Done consuming on a . or ?, turn off consumption state
                    sequence.pop(0)
                    consuming = False
                    continue
            elif c == ".":
                # Found . while consuming
                res = 0
                break
            # Consume this character
            sequence[0] -= 1
            continue

        # Not consuming
        if c == '?':
            # Split into two options
            res += solve_partial('.' + field[i+1:], tuple(sequence), sub_solutions)
            res += solve_partial('#' + field[i+1:], tuple(sequence), sub_solutions)
            break
        if c == '#':
            # Start consumption
            consuming = True
            sequence[0] -= 1
            continue
        else:  # c == '.'
            continue
    # End loop
    else:
        if res == 0 and (len(sequence) == 0 or (len(sequence) == 1 and sequence == [0])):
            # Ended field while exactly consuming the input
            res = 1

    # Record solution of this input
    sub_solutions[(field, given_sequence)] = res
    return res


def read_input(factor: int = 1):
    values = []
    with open('input/day12.txt') as input_file:
        for line in input_file:
            field, sequence = line.rstrip().split(" ")
            field = "?".join([field]*factor)
            sequence = ",".join([sequence]*factor)
            sequence = tuple(int(n) for n in sequence.split(','))
            values.append((field, sequence))
    return values
