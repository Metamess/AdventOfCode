
def part1():
    """
    XMAS starts by transmitting a preamble of 25 numbers.
    After that, each number you receive should be the sum of any two of the 25 immediately previous numbers.
    The two numbers will have different values, and there might be more than one such pair.
    Find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it.
    """
    xmas_numbers = read_input()
    sums = []
    preamble_size = 25
    # Create a list of (number, sums) tuples
    for i, number in enumerate(xmas_numbers[:preamble_size]):
        new_tuple = (number, [])
        for other in xmas_numbers[i+1: preamble_size]:
            new_tuple[1].append(number + other)
        sums.append(new_tuple)

    for i, number in enumerate(xmas_numbers[preamble_size:], preamble_size):
        # First check if the new number is a sum of two previous numbers
        found = False
        for sum_tuples in sums:
            if number in sum_tuples[1]:
                found = True
                break
        if not found:
            print(number)
            return
        # Add this number to the sum lists, add a new tuple, and remove the old one
        for sum_tuples in sums:
            sum_tuples[1].append(sum_tuples[0] + number)
        sums.pop(0)
        sums.append((number, []))
    print("Unable to find invalid number")


def part2():
    """
    You must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    Add together the smallest and largest number in this contiguous range.
    """
    part1_answer = 27911108
    xmas_numbers = read_input()
    for i in range(len(xmas_numbers)):
        total = 0
        counter = i
        while total < part1_answer:
            total += xmas_numbers[counter]
            counter += 1
        if total == part1_answer:
            min_value, max_value = min(xmas_numbers[i:counter]), max(xmas_numbers[i:counter])
            print(min_value + max_value)
            return


def read_input():
    numbers = []
    with open('input/day9.txt') as input_file:
        for line in input_file:
            numbers.append(int(line))
    return numbers
