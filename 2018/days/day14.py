
def part1():
	"""
	Only two recipes are on the board: the first recipe got a score of 3, the second, 7.
	Each of the two Elves has a current recipe: the first Elf starts with the first recipe,
	and the second Elf starts with the second recipe.
	To create new recipes, the two Elves combine their current recipes.
	This creates new recipes from the digits of the sum of the current recipes' scores.
	The new recipes are added to the end of the scoreboard in the order they are created.
	After all new recipes are added to the scoreboard, each Elf picks a new current recipe.
	To do this, the Elf steps forward through the scoreboard a number of recipes equal to 1 plus the score of their current recipe.
	If they run out of recipes, they loop back around to the beginning.
	What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?
	"""
	recipes = [3, 7]
	current_recipe_ids = [0, 1]

	with open('input/day14.txt') as input_file:
		desired_recipe_count = int(input_file.readline())

	while len(recipes) < desired_recipe_count + 10:
		# combination phase
		combination = recipes[current_recipe_ids[0]] + recipes[current_recipe_ids[1]]
		new_recipes = str(combination)
		for recipe in new_recipes:
			recipes.append(int(recipe))
		# pick a new recipe
		for i, current_id in enumerate(current_recipe_ids):
			current_recipe_ids[i] = (current_id + 1 + recipes[current_id]) % len(recipes)
	print(''.join(str(score) for score in recipes[desired_recipe_count:desired_recipe_count+10]))


def part2():
	"""
	How many recipes appear on the scoreboard to the left of the score sequence in your puzzle input?
	"""
	recipes = [3, 7]
	current_recipe_ids = [0, 1]

	with open('input/day14.txt') as input_file:
		sequence = [int(x) for x in input_file.readline().rstrip('\n')]

	while True:
		# combination phase
		combination = recipes[current_recipe_ids[0]] + recipes[current_recipe_ids[1]]
		new_recipes = str(combination)
		for recipe in new_recipes:
			recipes.append(int(recipe))
		# pick a new recipe
		for i, current_id in enumerate(current_recipe_ids):
			current_recipe_ids[i] = (current_id + 1 + recipes[current_id]) % len(recipes)

		if sequence == recipes[-len(sequence):]:
			print(len(recipes) - len(sequence))
			break
		elif sequence == recipes[-len(sequence)-1:-1]:
			print(len(recipes) - len(sequence) - 1)
			break
