def part1():
    """
    Each of your joltage adapters is rated for a specific output joltage (your puzzle input).
    Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
    Treat the charging outlet near your seat as having an effective joltage rating of 0.
    In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.
    Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter,
    and count the joltage differences between the charging outlet, the adapters, and your device.
    What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
    """
    adapters = read_input()
    adapters.sort()
    diff_count = {1: 0, 2: 0, 3: 1}  # Add one diff of 3 for your device
    prev = 0
    for adapter in adapters:
        diff_count[adapter-prev] += 1
        prev = adapter
    print(diff_count[1] * diff_count[3])


def part2():
    """
    What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
    """
    adapters = read_input()
    adapters.sort()
    ways = {0: 1}  # The number of ways from adapter A to 0 is the sum of ways for A-1, A-2 and A-3 if available
    for adapter in adapters:
        ways[adapter] = sum([ways[adapter-i] if adapter-i in ways else 0 for i in range(1, 4)])
    print(ways[adapters[-1]])


def read_input():
    adapters = []
    with open('input/day10.txt') as input_file:
        for line in input_file:
            adapters.append(int(line))
    return adapters
