from itertools import cycle


def part1():
    """
    As input, FFT takes a list of numbers, each number is a single digit.
    FFT operates in repeated phases. In each phase, a new list is constructed with the same length as the input list.
    This new list is also used as the input for the next phase.
    Each element in the new list is built by multiplying every value in the input list by a value in a repeating pattern and then adding up the results.
    While each element in the output array uses all of the same input array elements, the actual repeating pattern to use depends on which output element is being calculated.
    The base pattern is 0, 1, 0, -1. Then, repeat each value in the pattern a number of times equal to the position in the output list being considered.
    When applying the pattern, skip the very first value exactly once.
    After 100 phases of FFT, what are the first eight digits in the final output list?
    """
    signal = read_input()
    base_pattern = [0, 1, 0, -1]
    for _ in range(100):  # Repeat FFT 100 times
        next_signal = []
        for i in range(len(signal)):  # Calculate each signal element
            pattern = cycle(d for d in base_pattern for _ in range(i + 1))
            next(pattern)
            next_element = 0
            for d in signal:
                next_element += d*next(pattern)
            next_signal.append(abs(next_element) % 10)
        signal = next_signal
    print(''.join(str(c) for c in signal[:8]))


def part2():
    """

    """
    pass


def read_input():
    with open('input/day16.txt') as input_file:
        return [int(d) for d in input_file.readline().strip()]
