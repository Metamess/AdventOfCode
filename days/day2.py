from collections import defaultdict


def part1():
	"""
	To make sure you didn't miss any, you scan the likely candidate boxes again,
	counting the number that have an ID containing exactly two of any letter
	and then separately counting those with exactly three of any letter.
	You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
	"""
	double_counter = 0
	triple_counter = 0
	with open("input/day2.txt") as box_ids:
		for box_id in box_ids:
			char_counts = defaultdict(lambda: 0)
			for char in box_id:
				char_counts[char] += 1
			if 2 in char_counts.values():
				double_counter += 1
			if 3 in char_counts.values():
				triple_counter += 1
	print(double_counter*triple_counter)


def part2():
	"""
	The boxes will have IDs which differ by exactly one character at the same position in both strings.
	What letters are common between the two correct box IDs?
	"""
	common_letters = []
	with open("input/day2.txt") as box_ids:
		for box_id in box_ids:
			while len(common_letters) < len(box_id):
				common_letters.append(set())
			for i in range(len(box_id)):
				reduced_id = box_id[:i] + box_id[i+1:]
				if reduced_id in common_letters[i]:
					print(reduced_id)
					return
				common_letters[i].add(reduced_id)
