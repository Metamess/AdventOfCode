
def part1():
	"""
	The tree is made up of nodes;
	Specifically, a node consists of:
		A header, which is always exactly two numbers:
			The quantity of child nodes.
			The quantity of metadata entries.
		Zero or more child nodes (as specified in the header).
		One or more metadata entries (as specified in the header).
	What is the sum of all metadata entries?
	"""
	with open('input/day8.txt') as input_file:
		tree_as_list = input_file.readline().split(' ')
	for i in range(len(tree_as_list)):
		tree_as_list[i] = int(tree_as_list[i])

	def process_node(input_list):
		my_sum = 0
		children = input_list.pop(0)
		metadata_entries = input_list.pop(0)
		for i in range(children):
			my_sum += process_node(input_list)
		for i in range(metadata_entries):
			my_sum += input_list.pop(0)
		return my_sum

	print(process_node(tree_as_list))


def part2():
	"""
	If a node has no child nodes, its value is the sum of its metadata entries.
	However, if a node does have child nodes, the metadata entries become indexes which refer to those child nodes.
	The value of this node is the sum of the values of the child nodes referenced by the metadata entries.
	If a referenced child node does not exist, that reference is skipped.
	A child node can be referenced multiple time and counts each time it is referenced.
	A metadata entry of 0 does not refer to any child node.
	What is the value of the root node?
	"""
	with open('input/day8.txt') as input_file:
		tree_as_list = input_file.readline().split(' ')
	for i in range(len(tree_as_list)):
		tree_as_list[i] = int(tree_as_list[i])

	def process_node(input_list):
		my_value = 0
		child_count = input_list.pop(0)
		child_values = [0 for _ in range(child_count + 1)]
		metadata_entry_count = input_list.pop(0)
		for i in range(child_count):
			child_values[i+1] = process_node(input_list)
		for i in range(metadata_entry_count):
			if child_count == 0:
				my_value += input_list.pop(0)
			else:
				child_reference = input_list.pop(0)
				if 0 < child_reference <= child_count:
					my_value += child_values[child_reference]
		return my_value

	print(process_node(tree_as_list))
