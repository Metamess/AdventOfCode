def part1():
    """
    """
    instructions = read_input()
    return sum(holiday_hash(s) for s in instructions)


def part2():
    """
    """
    instructions = read_input()
    boxes = [{} for _ in range(256)]
    for instruction in instructions:
        if instruction.endswith('-'):
            label = instruction[:-1]
            box_nr = holiday_hash(label)
            try:
                boxes[box_nr].pop(label)
            except KeyError:
                pass
            continue
        label, length = instruction.split('=')
        box_nr = holiday_hash(label)
        boxes[box_nr][label] = int(length)
    total = 0
    for box_nr, box in enumerate(boxes):
        for lens_nr, focal_length in enumerate(box.values()):
            total += (box_nr + 1) * (lens_nr + 1) * focal_length
    return total


def holiday_hash(string: str) -> int:
    res = 0
    for c in string:
        res = ((res + ord(c)) * 17) % 256
    return res


def read_input():
    with open('input/day15.txt') as input_file:
        return input_file.read().split(',')
