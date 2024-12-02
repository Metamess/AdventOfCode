import math


def part1():
    """
    """
    result = 0
    for game_id, rounds in read_input().items():
        if all([info.get("red", 0) <= 12 and info.get("green", 0) <= 13 and info.get("blue", 0) <= 14 for info in rounds]):
            result += game_id
    return result


def part2():
    """
    """
    result = 0
    for game_id, rounds in read_input().items():
        minimums = [max(info.get(color, 0) for info in rounds) for color in ["red", "green", "blue"]]
        result += math.prod(minimums)
    return result


def read_input():
    games = {}
    with open('input/day2.txt') as input_file:
        for line in input_file:
            game, content = line.rstrip().split(": ")
            game_id = int(game.split(" ")[-1])
            for rounds in content.split("; "):
                info = {}
                for color_info in rounds.split(", "):
                    count, color = color_info.split(" ")
                    info[color] = int(count)
                games.setdefault(game_id, []).append(info)
    return games
