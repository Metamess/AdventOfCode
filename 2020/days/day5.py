
def part1():
    """
    this airline uses binary space partitioning to seat people.
    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane [F=0, B=1]
    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane =[L=0, R=1]
    Every seat also has a unique seat ID: multiply the row by 8, then add the column.
    As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
    """
    boarding_passes = read_input()
    max_id = 0
    for seat in boarding_passes:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(seat[8:].replace('L', '0').replace('R', '1'), 2)
        max_id = max(max_id, column + row*8)
    print(max_id)


def part2():
    """
    Some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
    Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
    What is the ID of your seat?
    """
    boarding_passes = read_input()
    seat_numbers = []
    for seat in boarding_passes:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        seat_numbers.append(column + row * 8)
    seat_numbers.sort()
    prev = 0
    for seat in seat_numbers:
        if seat-prev == 2:
            print(seat-1)
            break
        prev = seat


def read_input():
    boarding_passes = []
    with open('input/day5.txt') as input_file:
        for line in input_file:
            boarding_passes.append(line.rstrip())
    return boarding_passes
