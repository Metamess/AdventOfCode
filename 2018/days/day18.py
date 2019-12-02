from collections import Counter


def part1(time=10):
    """
    What will the total resource value of the lumber collection area be after 10 minutes?
    """
    forest = Forest(read_input())
    for minute in range(time):
        forest.simulate_minute()
    print(forest.get_value())


def part2():
    """
    What will the total resource value of the lumber collection area be after 1000000000 minutes?
    """
    # Look for a repeating pattern
    final_minute = 1000000000
    forest = Forest(read_input())
    forest_dict = {}
    reoccurrence = None
    for t in range(final_minute):
        forest_string = str(forest)
        if forest_string in forest_dict:
            reoccurrence = t
            break
        forest_dict[forest_string] = t
        forest.simulate_minute()
    # A cycle has been detected, so we can skip ahead
    first_occurence = forest_dict[str(forest)]
    remainder = (final_minute-first_occurence) % (reoccurrence - first_occurence)
    for i in range(remainder):
        forest.simulate_minute()
    print(forest.get_value())


def read_input():

    with open('input/day18.txt') as input_file:
        forest = []
        for line in input_file:
            forest.append(list(line.rstrip('\n')))
    return forest


class Forest:

    def __init__(self, forest):
        self.forest = forest
        self.time = 0

    def simulate_minute(self):
        new_forest = []
        for y in range(len(self.forest)):
            new_forest.append([])
            for x in range(len(self.forest[y])):
                here = self.forest[y][x]
                s = self.get_surroundings(x, y)
                if here == '.' and s['|'] > 2:
                    new_forest[-1].append('|')
                elif here == '|' and s['#'] > 2:
                    new_forest[-1].append('#')
                elif here == '#' and (s['#'] == 0 or s['|'] == 0):
                    new_forest[-1].append('.')
                else:
                    new_forest[-1].append(here)
        self.forest = new_forest
        self.time += 1

    def get_surroundings(self, x, y):
        surroundings = Counter()
        if y > 0:
            surroundings.update(self.forest[y - 1][max(0, x - 1):min(len(self.forest[y]), x + 2)])
        surroundings.update(self.forest[y][max(0, x - 1):min(len(self.forest[y]), x + 2)])
        surroundings.subtract([self.forest[y][x]])
        if y < len(self.forest) - 1:
            surroundings.update(self.forest[y + 1][max(0, x - 1):min(len(self.forest[y]), x + 2)])
        return surroundings

    def get_value(self):
        woods = sum(self.forest[i].count('|') for i in range(len(self.forest)))
        yards = sum(self.forest[i].count('#') for i in range(len(self.forest)))
        return woods * yards

    def __str__(self):
        return ''.join([''.join(self.forest[y]) for y in range(len(self.forest))])
