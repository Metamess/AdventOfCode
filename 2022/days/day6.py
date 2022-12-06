
def part1():
    """
    You need to detect a start-of-packet marker in the datastream.
    The start of a packet is indicated by a sequence of four characters that are all different.
    How many characters need to be processed before the first start-of-packet marker is detected?
    """
    stream = read_input()
    return single_pass_solution(4, stream)


def part2():
    """
    A start-of-message marker is just like a start-of-packet marker,
    except it consists of 14 distinct characters rather than 4.
    How many characters need to be processed before the first start-of-message marker is detected?
    """
    stream = read_input()
    return single_pass_solution(14, stream)


def simple_solution(header_size: int, stream: str) -> int | None:
    for i in range(header_size, len(stream) + 1):
        if len(set(stream[i - header_size:i])) == header_size:
            return i
    return None


def single_pass_solution(header_size: int, stream: str) -> int | None:
    # input consists only of lowercase letters
    last_seen = [0] * 26
    offset = ord('a')
    duplicate_until = 0
    for i in range(len(stream)):
        char_code = ord(stream[i]) - offset
        prev_char = last_seen[char_code]
        if prev_char > i - header_size:
            duplicate_until = max(duplicate_until, prev_char + header_size)
        last_seen[char_code] = i
        if i >= duplicate_until:
            return i + 1  # i is a 0-based index, but the desired answer is ordinal
    return None


def read_input():
    with open('input/day6.txt') as input_file:
        return input_file.readline().rstrip()
