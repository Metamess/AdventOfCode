from collections import defaultdict
import math


def part1():
    """
    Every reaction turns some quantities of specific input chemicals into some quantity of an output chemical.
    You just need to know how much ORE you'll need to collect before you can produce one unit of FUEL.
    """
    recipes = read_input()
    need = defaultdict(int, FUEL=1)
    have = defaultdict(int)
    in_need = True
    while in_need:
        in_need = False
        for material in need:
            if material != 'ORE' and need[material] > have[material]:
                in_need = True
                for ingredients in recipes[material][1:]:
                    need[ingredients[0]] += ingredients[1]
                have[material] += recipes[material][0]
                break
    print(need['ORE'])


def part2():
    """
    Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?
    """
    trillion = 10**12
    recipes = read_input()
    need = defaultdict(int, FUEL=1)
    have = defaultdict(int)
    in_need = True
    while in_need:
        in_need = False
        for material in need:
            if material != 'ORE' and need[material] > have[material]:
                in_need = True
                times_needed = math.ceil((need[material] - have[material]) / recipes[material][0])
                for ingredients in recipes[material][1:]:
                    need[ingredients[0]] += times_needed*ingredients[1]
                have[material] += times_needed*recipes[material][0]
                break
        if not in_need:
            current_ore = need['ORE']
            current_fuel = have['FUEL']
            ratio = trillion / current_ore
            # print(current_fuel, 'fuel requires', current_ore, 'ore, with a ratio of ', ratio)
            if int(ratio) > 1:
                need['FUEL'] = int(current_fuel * ratio)
                in_need = True
            elif current_ore < trillion:
                current_fuel = have['FUEL']
                need['FUEL'] += 1
                in_need = True
    print(need['FUEL']-1)


def read_input():
    recipes = dict()
    with open('input/day14.txt') as input_file:
        for line in input_file:
            ingredients, results = line.strip().split(' => ')
            res_amount, res_material = results.split(' ')
            res = [int(res_amount)]
            for ingredient in ingredients.split(', '):
                amount, material = ingredient.split(' ')
                res.append([material, int(amount)])
            assert res_material not in recipes
            recipes[res_material] = res
    return recipes
