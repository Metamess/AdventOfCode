
def part1():
    """
    The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
    The second column is what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    What would your total score be if everything goes exactly according to your strategy guide?
    """
    rounds = read_input()
    shape_scores = [1, 2, 3]
    result_scores = [3, 0, 6]
    score = 0
    for them, you in rounds:
        score += shape_scores[you]
        score += result_scores[them - you]
    return score


def part2():
    """
    The second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a
    draw, and Z means you need to win. What would your total score?
    """
    rounds = read_input()
    shape_scores = [1, 2, 3]
    result_scores = [0, 3, 6]
    score = 0
    for them, result in rounds:
        score += shape_scores[(them + result - 1) % 3]
        score += result_scores[result]
    return score


def read_input():
    values = []
    with open('input/day2.txt') as input_file:
        for line in input_file:
            values.append([ord(line[0]) - ord('A'), ord(line[2]) - ord('X')])
    return values
