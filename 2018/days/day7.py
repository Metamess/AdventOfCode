from collections import defaultdict


def part1():
	"""
	Your first goal is to determine the order in which the steps should be completed.
	If more than one step is ready, choose the step which is first alphabetically.
	In what order should the steps in your instructions be completed?
	"""
	instructions = InstructionGraph()
	instructions.read_instructions()
	res = instructions.execute_sequentially()
	print(''.join(res))


def part2():
	"""
	With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?
	"""
	instructions = InstructionGraph()
	instructions.read_instructions()
	res = instructions.execute_simultaneously(5)
	print(res)


class Step:

	def __init__(self):
		self.depends_on = set()
		self.makes_available = set()

	@staticmethod
	def get_duration(letter):
		return ord(letter) - 4  # ord('A') = 65


class InstructionGraph:

	def __init__(self):
		self.available_steps = set()
		self.steps = defaultdict(Step)

	def read_instructions(self, input_path="input/day7.txt"):
		unavailable_steps = set()
		# Step A must be finished before step B can begin.
		with open(input_path) as instructions:
			for instruction in instructions:
				step_a = instruction[5]
				step_b = instruction[36]
				self.steps[step_a].makes_available.add(step_b)
				self.available_steps.add(step_a)
				self.steps[step_b].depends_on.add(step_a)
				unavailable_steps.add(step_b)
		self.available_steps -= unavailable_steps

	def execute_sequentially(self):
		next_steps = sorted(self.available_steps)
		executed_steps = []
		while len(executed_steps) < len(self.steps):
			assert len(next_steps) > 0
			current_step_id = next_steps.pop(0)
			for step_id in self.steps[current_step_id].makes_available:
				self.steps[step_id].depends_on.remove(current_step_id)
				if len(self.steps[step_id].depends_on) == 0:
					next_steps.append(step_id)
			next_steps.sort()
			executed_steps.append(current_step_id)
		return executed_steps

	def execute_simultaneously(self, worker_count=5):
		worker_status = [['.', 0] for _ in range(worker_count)]
		next_steps = sorted(self.available_steps)
		executed_steps = []
		timer = -1

		while len(executed_steps) < len(self.steps):
			timer += 1
			for worker in worker_status:
				if worker[0] != '.':
					worker[1] -= 1
					if worker[1] == 0:
						# If the worker is done with the step, signal all steps depending on it that it's done
						for step_id in self.steps[worker[0]].makes_available:
							self.steps[step_id].depends_on.remove(worker[0])
							# If this was the last remaining dependency, add this step to the available steps
							if len(self.steps[step_id].depends_on) == 0:
								next_steps.append(step_id)
						next_steps.sort()
						executed_steps.append(worker[0])
						worker[0] = '.'
			# Give jobs to idle workers
			for worker in worker_status:
				if worker[0] == '.':
					if len(next_steps) > 0:
						worker[0] = next_steps.pop(0)
						worker[1] = Step.get_duration(worker[0])

		return timer
