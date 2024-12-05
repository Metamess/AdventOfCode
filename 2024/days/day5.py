def part1():
    """
    """
    rules, manuals = read_input()
    res = 0
    for manual in manuals:
        for i, page in enumerate(manual):
            if page not in rules:
                continue
            if rules[page].intersection(set(manual[:i])):
                break
        else:
            res += int(manual[len(manual)//2])
    return res


def part2():
    """
    """
    rules, manuals = read_input()
    res = 0
    wrong_manuals = []
    for manual in manuals:
        for i, page in enumerate(manual):
            if page not in rules:
                continue
            if rules[page].intersection(set(manual[:i])):
                wrong_manuals.append(manual)
                break

    while wrong_manuals:
        manual = wrong_manuals.pop()
        for i, page in enumerate(manual):
            if page not in rules:
                continue
            conflicts = rules[page].intersection(set(manual[:i]))
            if conflicts:
                min_id = min(manual.index(c) for c in conflicts)
                fixed_manual = manual[:min_id] + [manual[i]] + manual[min_id:i] + manual[i + 1:]
                wrong_manuals.append(fixed_manual)
                break
        else:
            res += int(manual[len(manual) // 2])
    return res


def read_input() -> tuple[dict[str, set[str]], list[list[str]]]:
    rules = {}
    manuals = []
    with open('input/day5.txt') as input_file:
        rules_section = True
        for line in input_file:
            line = line.rstrip()
            if rules_section:
                if not line:
                    rules_section = False
                    continue
                a, b = line.split('|')
                rules.setdefault(a, set()).add(b)
            else:
                manuals.append(line.split(','))
    return rules, manuals
