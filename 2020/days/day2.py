
def part1():
    """
    Each line gives the password policy and then the password.
    The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
    How many passwords are valid according to their policies?
    """
    password_dump = read_input()
    valid_count = 0
    for lower, upper, letter, password in password_dump:
        if lower <= password.count(letter) <= upper:
            valid_count += 1
    print(valid_count)


def part2():
    """
    Each policy actually describes two positions in the password, where 1 means the first character.
    Exactly one of these positions must contain the given letter.
    How many passwords are valid according to the new interpretation of the policies?
    """
    password_dump = read_input()
    valid_count = 0
    for first, second, letter, password in password_dump:
        if int(password[first-1] == letter) + int(password[second-1] == letter) == 1:
            valid_count += 1
    print(valid_count)


def read_input():
    password_dump = []
    with open('input/day2.txt') as input_file:
        for line in input_file:
            constraint, letter, password = line.rstrip('\n').split(' ')
            lower_constraint, upper_constraint = [int(c) for c in constraint.split('-')]
            letter = letter[0]
            password_dump.append([lower_constraint, upper_constraint, letter, password])
    return password_dump
