from collections import deque, defaultdict


def part1():
	"""
	First, the marble numbered 0 is placed in the circle. This marble is designated the current marble.
	Then, each Elf takes a turn placing the lowest-numbered remaining marble into the circle,
	between the marbles that are 1 and 2 marbles clockwise of the current marble.
	The marble that was just placed then becomes the current marble.

	However, if the marble that is about to be placed has a number which is a multiple of 23,
	something entirely different happens.
	First, the current player keeps the marble they would have placed, adding it to their score.
	In addition, the marble 7 marbles counter-clockwise from the current marble is removed from the circle,
	and also added to the current player's score.
	The marble located immediately clockwise of the marble that was removed becomes the new current marble.
	What is the winning Elf's score?
	"""
	players, marbles = parse_input()
	print(play_marble_game(players, marbles))


def part2():
	"""
	What would the new winning Elf's score be if the number of the last marble were 100 times larger?
	"""
	players, marbles = parse_input()
	print(play_marble_game(players, marbles*100))


def parse_input():
	with open('input/day9.txt') as games:
		game_parameters = games.readline().split(' ')
		players = int(game_parameters[0])
		marbles = int(game_parameters[6])
	return players, marbles


def play_marble_game(players, marbles):
	circle = deque([0])
	scores = defaultdict(int)
	mod_23_counter = 1
	current_player = 1
	for marble_value in range(1, marbles+1):
		# Handle case for every 23rd marble
		if mod_23_counter == 23:
			assert marble_value % 23 is 0
			mod_23_counter = 0
			# Bring the marble 7 positions counter-clockwise to the front, and pop it
			circle.rotate(7)
			scores[current_player] += circle.pop() + marble_value
			circle.rotate(-1)

		# Default case where marbles are added
		else:
			circle.rotate(-1)
			circle.append(marble_value)

		# Use counters rather than modulo operators
		if current_player == players:
			current_player = 0
		mod_23_counter += 1
		current_player += 1

	# Return the high-score as result
	return max(scores.values())
