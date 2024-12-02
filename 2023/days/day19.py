import math


def part1():
    """
    """
    with open('input/day19.txt') as input_file:
        workflows_input, parts_input = input_file.read().split('\n\n')

    workflows = {}
    for workflow in sorted(workflows_input.split()):
        # rbs{m>562:A,a<333:A,A}
        name, rules_input = workflow[:-1].split('{')
        lambda_str = "lambda part: "
        for rule in rules_input.split(','):
            if ':' in rule:
                condition, result = rule.split(':')
                lambda_str += f"'{result}' if part['{condition[0]}']{condition[1:]} else "
            else:
                lambda_str += f"'{rule}'"
        workflows[name] = eval(lambda_str)

    parts = []
    for part in parts_input.split():
        parts.append(eval(part.replace('{', '{"').replace('=', '":').replace(',', ',"')))

    total = 0
    for part in parts:
        state = "in"
        while state not in ["A", "R"]:
            state = workflows[state](part)
        if state == "A":
            total += sum(part.values())
    return total


def part2():
    """
    """
    workflows = {}
    with open('input/day19.txt') as input_file:
        workflows_input, _ = input_file.read().split('\n\n')
    for workflow in workflows_input.split():
        # rbs{m>562:A,a<333:A,A}
        name, rules_input = workflow[:-1].split('{')
        rules = []
        for rule_str in rules_input.split(','):
            if ':' in rule_str:
                condition, result = rule_str.split(':')
                if '<' in condition:
                    key, threshold = condition.split('<')
                    condition = '<'
                else:
                    key, threshold = condition.split('>')
                    condition = '>'
                rules.append((key, condition, int(threshold), result))
            else:
                rules.append(rule_str)
        workflows[name] = rules

    total = 0
    parts = [("in", {k: 1 for k in "xmas"}, {k: 4000 for k in "xmas"})]
    while parts:
        state, min_values, max_values = parts.pop()
        if state == "R":
            continue
        if state == "A":
            total += math.prod(max_values[k] - min_values[k] + 1 for k in "xmas")
            continue
        workflow = workflows[state]
        for key, condition, threshold, result in workflow[:-1]:
            if condition == '<':
                if max_values[key] < threshold:
                    # entire part passes, put back on queue with new state
                    parts.append((result, min_values, max_values))
                    break
                else:
                    # split part, queue compliant part
                    compliant_part = (result, min_values.copy(), max_values.copy())
                    compliant_part[2][key] = threshold - 1
                    parts.append(compliant_part)
                    min_values[key] = threshold
            else:
                assert condition == '>'
                if min_values[key] > threshold:
                    # entire part passes, put back on queue with new state
                    parts.append((result, min_values, max_values))
                    break
                else:
                    # split part, queue compliant part
                    compliant_part = (result, min_values.copy(), max_values.copy())
                    compliant_part[1][key] = threshold + 1
                    parts.append(compliant_part)
                    max_values[key] = threshold
        else:
            # Default option for workflow, queue part with new state
            parts.append((workflow[-1], min_values, max_values))

    return total
