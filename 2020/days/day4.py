import string


def part1():
    """
    Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
    Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
    """
    passport_list = read_input()
    valid = 0
    for passport in passport_list:
        if len(passport) == 8:
            valid += 1
        elif len(passport) == 7:
            if 'cid' not in passport:
                valid += 1
    print(valid)


def part2():
    """
    Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    passport_list = read_input()
    valid = 0
    for passport in passport_list:
        if not (len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport)):
            continue
        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue
        if len(passport['hgt']) <= 2:
            continue
        height_value, height_unit = int(passport['hgt'][:-2]), passport['hgt'][-2:]
        if not ((height_unit == 'cm' and 150 <= height_value <= 193)
                or (height_unit == 'in' and 59 <= height_value <= 76)):
            continue
        if not (len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all(c in string.hexdigits for c in passport['hcl'][1:])):
            continue
        if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if not (len(passport['pid']) == 9 and passport['pid'].isdecimal()):
            continue
        valid += 1
    print(valid)


def read_input():
    passport_list = [dict()]
    with open('input/day4.txt') as input_file:
        for line in input_file:
            if line == '\n':
                passport_list.append(dict())
                continue
            for pair in line.rstrip('\n').split(' '):
                k, v = pair.split(':')
                passport_list[-1][k] = v
    return passport_list
