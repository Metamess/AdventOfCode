
def part1():
    """
    The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
    The following rules are applied to every seat simultaneously:
    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change.
    Simulate your seating area by applying the seating rules repeatedly until no seats change state.
    How many seats end up occupied?
    """
    seats_current = read_input()
    changes = 1
    while changes > 0:
        changes = 0
        seats_next = []
        for j, seats_row in enumerate(seats_current):
            seat_row_next = []
            for i, seat in enumerate(seats_row):
                if seat == '.':
                    seat_row_next.append('.')
                    continue
                filled_adjacent = sum([seats_current[k][max(0, i-1):min(len(seats_row), i+2)].count('#') for k in range(max(0, j-1), min(len(seats_current), j+2))]) - (1 if seat == '#' else 0)
                if seat == 'L' and filled_adjacent == 0:
                    seat_row_next.append("#")
                    changes += 1
                elif seat == '#' and filled_adjacent >= 4:
                    seat_row_next.append("L")
                    changes += 1
                else:
                    seat_row_next.append(seat)
            seats_next.append(seat_row_next)
        seats_current = seats_next
    print(sum([seats_row.count("#") for seats_row in seats_current]))


def part2():
    """
    Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions.
    Also, it now takes five or more visible occupied seats for an occupied seat to become empty.
    Once equilibrium is reached, how many seats end up occupied?
    """
    seats_current = read_input()

    def get_filled_adjacent(x, y):
        filled = 0
        for delta_x in range(-1, 2):
            for delta_y in range(-1, 2):
                if delta_x == 0 and delta_y == 0:
                    continue  # Skip checking yourself
                iteration = 1
                while True:
                    new_x = x + delta_x * iteration
                    new_y = y + delta_y * iteration
                    if not (0 <= new_x < len(seats_current[0]) and 0 <= new_y < len(seats_current)):
                        break  # No seat found before edge reached
                    seat_in_view = seats_current[new_y][new_x]
                    if seat_in_view == '.':
                        iteration += 1
                        continue
                    elif seat_in_view == '#':
                        filled += 1
                        break
                    else:
                        assert seat_in_view == 'L'
                        break
        return filled

    changes = 1
    while changes > 0:
        changes = 0
        seats_next = []
        for j, seats_row in enumerate(seats_current):
            seat_row_next = []
            for i, seat in enumerate(seats_row):
                if seat == '.':
                    seat_row_next.append('.')
                    continue
                filled_adjacent = get_filled_adjacent(i, j)
                if seat == 'L' and filled_adjacent == 0:
                    seat_row_next.append("#")
                    changes += 1
                elif seat == '#' and filled_adjacent >= 5:
                    seat_row_next.append("L")
                    changes += 1
                else:
                    seat_row_next.append(seat)
            seats_next.append(seat_row_next)
        seats_current = seats_next
    print(sum([seats_row.count("#") for seats_row in seats_current]))


def read_input():
    seats = []
    with open('input/day11.txt') as input_file:
        for line in input_file:
            seats.append(list(line.rstrip()))
    return seats
