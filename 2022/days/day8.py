import itertools


def part1():
    """
    The expedition comes across a peculiar patch of tall trees all planted carefully in a grid.
    Count the number of trees that are visible from outside the grid when looking directly along a row or column.
    Each tree is represented as a single digit whose value is its height.
    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
    How many trees are visible from outside the grid?
    """
    forest = read_input()
    row_length = len(forest[0])
    column_length = len(forest)
    marked_as_visible = [[False] * row_length for _ in range(column_length)]
    count = 0
    # Somewhat convoluted way to loop over both rows and columns in both directions without repeating any logic
    for along_row in [True, False]:
        for ascending in [True, False]:
            range_other_axis = range(column_length if along_row else row_length)
            for i in range_other_axis:
                range_along_axis = range(row_length if along_row else column_length)
                if not ascending:
                    range_along_axis = reversed(range_along_axis)
                tallest = -1
                for j in range_along_axis:
                    row_id, column_id = (j, i) if along_row else (i, j)
                    tree_size = forest[column_id][row_id]
                    if tree_size > tallest:
                        tallest = tree_size
                        if not marked_as_visible[column_id][row_id]:
                            count += 1
                            marked_as_visible[column_id][row_id] = True
    return count


def part2():
    """
    The Elves would like to be able to see a lot of trees.
    To measure the viewing distance from a given tree, look up, down, left, and right from that tree;
    Stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration.
    The Elves don't care about distant trees taller than those found by the rules above.
    A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
    What is the highest scenic score possible for any tree?
    """
    forest = read_input()
    row_length = len(forest[0])
    column_length = len(forest)
    high_score = 0
    for candidate_i in range(1, column_length - 1):
        for candidate_j in range(1, row_length - 1):
            tree_size = forest[candidate_i][candidate_j]
            score = 1
            left = zip(itertools.repeat(candidate_i), range(candidate_j - 1, -1, -1))
            right = zip(itertools.repeat(candidate_i), range(candidate_j + 1, row_length))
            up = zip(range(candidate_i - 1, -1, -1), itertools.repeat(candidate_j))
            down = zip(range(candidate_i + 1, column_length), itertools.repeat(candidate_j))
            for direction_coordinates in (up, down, left, right):
                visible_trees = 0
                for i, j in direction_coordinates:
                    visible_trees += 1
                    if forest[i][j] >= tree_size:
                        break
                score *= visible_trees
            high_score = max(high_score, score)
    return high_score


def read_input():
    values = []
    with open('input/day8.txt') as input_file:
        for line in input_file:
            values.append([int(d) for d in line.rstrip()])
    return values
