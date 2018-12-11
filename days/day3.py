
def part1():
	"""
	The whole piece of fabric they're working on is a very large square.
	Each Elf has made a claim about which area of fabric would be ideal for Santa's suit.
	How many square inches of fabric are within two or more claims?
	"""
	fabric = Fabric()
	with open('input/day3.txt') as claim_strings:
		for claim_string in claim_strings:
			claim = Claim(claim_string)
			fabric.add_claim(claim)
	print(fabric.overlap_counter)


def part2():
	"""
	What is the ID of the only claim that doesn't overlap?
	"""
	fabric = Fabric()
	with open('input/day3.txt') as claim_strings:
		for claim_string in claim_strings:
			claim = Claim(claim_string)
			fabric.add_claim(claim)
	assert len(fabric.intact_claims) == 1
	print(fabric.intact_claims.pop())


class Claim:

	def __init__(self, input_string):
		"""
		:param input_string: String with format "#<ID> @ <left_margin>,<top_margin>: <width>x<height>"
		"""
		input_list = input_string.split(' ')
		self.claim_id = int(input_list[0][1:])
		margins = input_list[2][:-1].split(',')
		self.left_margin = int(margins[0])
		self.top_margin = int(margins[1])
		dimensions = input_list[3].split('x')
		self.width = int(dimensions[0])
		self.height = int(dimensions[1])


class Fabric:

	def __init__(self):
		self.fabric = [[]]
		self.overlap_counter = 0
		self.intact_claims = set()

	def add_claim(self, claim):
		self.adjust_size(claim)
		# apply claim to fabric, counting new overlaps and keeping track of claims that don't overlap
		overlap = False
		for y in range(claim.top_margin, claim.top_margin + claim.height):
			for x in range(claim.left_margin, claim.left_margin + claim.width):
				current_state = self.fabric[y][x]
				if current_state == ".":
					self.fabric[y][x] = claim.claim_id
				elif current_state == 'X':
					overlap = True
				else:
					overlap = True
					self.overlap_counter += 1
					if current_state in self.intact_claims:
						self.intact_claims.remove(current_state)
					self.fabric[y][x] = 'X'
		if not overlap:
			self.intact_claims.add(claim.claim_id)

	def adjust_size(self, claim):
		fabric_min_width = claim.left_margin + claim.width
		fabric_min_height = claim.top_margin + claim.height
		# adjust fabric dimensions to fit claim
		if len(self.fabric[0]) < fabric_min_width:
			for fabric_row in self.fabric:
				fabric_row += ['.'] * (fabric_min_width - len(fabric_row))
		while len(self.fabric) < fabric_min_height:
			self.fabric.append(['.'] * len(self.fabric[0]))
