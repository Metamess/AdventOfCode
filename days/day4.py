from collections import defaultdict


def part1():
	"""
	Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
	What is the ID of the guard you chose multiplied by the minute you chose?
	"""
	guards_data = process_sleeping_log()

	# get the most sleepy guard
	sleepyhead_id = -1
	max_time_asleep = -1
	for guard_id in guards_data:
		total_time_asleep = sum(guards_data[guard_id])
		if total_time_asleep > max_time_asleep:
			sleepyhead_id = guard_id
			max_time_asleep = total_time_asleep

	# find the minute most often spent asleep
	sleepy_minute = guards_data[sleepyhead_id].index(max(guards_data[sleepyhead_id]))
	print(sleepyhead_id * sleepy_minute)


def part2():
	"""
	Of all guards, which guard is most frequently asleep on the same minute?
	What is the ID of the guard you chose multiplied by the minute you chose?
	"""
	guards_data = process_sleeping_log()

	# get the minute most spent asleep
	max_times_asleep = -1
	sleepy_minute = -1
	sleepyhead_id = -1
	for guard_id in guards_data:
		for minute, amount_asleep in enumerate(guards_data[guard_id]):
			if amount_asleep > max_times_asleep:
				max_times_asleep = amount_asleep
				sleepy_minute = minute
				sleepyhead_id = guard_id
	print(sleepyhead_id * sleepy_minute)


def handle_time_asleep(guards_data, guard, fell_asleep_at, woke_up_at):
	for minute in range(fell_asleep_at, woke_up_at):
		guards_data[guard][minute] += 1


def process_sleeping_log():
	# Start by putting the logs in chronological order
	logs = []
	with open('input/day4.txt') as full_log:
		for log_entry in full_log:
			logs.append(log_entry)
	logs.sort()

	# gather sleeping data per guard per minute
	guards_data = defaultdict(lambda: [0] * 60)
	current_guard = -1
	fell_asleep_at = -1
	for log_entry in logs:
		if log_entry[19] == "G":  # Guard #<ID> starts shift
			# Handle case where previous guard slept past 1 AM
			if fell_asleep_at != -1:
				print("Sleepyhead!")
				assert current_guard != -1
				handle_time_asleep(guards_data, current_guard, fell_asleep_at, 60)
				fell_asleep_at = -1
			current_guard = int(log_entry.split(' ')[3][1:])

		elif log_entry[19] == "f":  # falls asleep
			assert fell_asleep_at == -1
			fell_asleep_at = int(log_entry[15:17])

		elif log_entry[19] == "w":  # wakes up
			assert fell_asleep_at != -1
			woke_up_at = int(log_entry[15:17])
			handle_time_asleep(guards_data, current_guard, fell_asleep_at, woke_up_at)
			fell_asleep_at = -1
	return guards_data


