def part1():
    """
    """
    seeds, maps = read_input()
    # Each seed range is a (start, end) tuple
    seed_ranges = [(seed, seed + 1) for seed in seeds]
    return get_lowest_number_after_maps(seed_ranges, maps)


def part2():
    """
    """
    seeds, maps = read_input()
    # Each seed range is a (start, end) tuple
    seed_ranges = [(start, start + size) for start, size in zip(seeds[::2], seeds[1::2])]
    return get_lowest_number_after_maps(seed_ranges, maps)


def get_lowest_number_after_maps(seed_ranges: list[tuple[int, int]], maps: dict[str, list[list[int]]]) -> int:
    # Sort map ranges descending by src per map, and value ranges descending by start, so we can consume them as a stack
    maps_list = [sorted(map_range, reverse=True) for map_range in maps.values()]
    value_ranges = sorted(seed_ranges, reverse=True)

    # Apply mapping for each map
    for i, map_ranges in enumerate(maps_list):
        next_map_value_ranges = []

        src_start, src_end, offset = 0, 0, 0
        while value_ranges:
            # Each value range is a (start, end) tuple
            val_start, val_end = value_ranges.pop()

            # Pop new map range while they are "behind" the current value range
            while map_ranges and val_start >= src_end:
                # Each map range is a (src, src_end, offset) tuple
                src_start, src_end, offset = map_ranges.pop()

            if val_start >= src_end:
                # There's no more map ranges, but still value ranges
                next_map_value_ranges.append((val_start, val_end))
                continue

            # Check for a value range before the map range
            if val_start < src_start:
                # Record any part of the value range that falls before the map range
                next_map_value_ranges.append((val_start, min(src_start, val_end)))
                if src_start <= val_end:
                    # Value range continues inside map range, add as new range to this iteration's stack
                    value_ranges.append((src_start, val_end))
                continue

            # There's a value range inside the map range, and these values get an offset
            inside = (max(src_start, val_start) + offset, min(val_end, src_end) + offset)
            next_map_value_ranges.append(inside)
            if val_end > src_end:
                # Value range continues outside of map range, add as new range to this iteration's stack
                value_ranges.append((src_end, val_end))

        # Sort the new value ranges in descending order
        value_ranges = sorted(next_map_value_ranges, reverse=True)

    return value_ranges[-1][0]


def read_input():
    with open('input/day5.txt') as input_file:
        # Read seeds and sort them
        seeds_line = input_file.readline().rstrip()
        seeds = [int(s) for s in seeds_line.split(" ")[1:]]
        line = input_file.readline()
        # Read all maps
        maps = {}
        while True:
            if not line:
                break
            # Read single map
            map_name = input_file.readline().split(" ")[0]
            map_ranges = []
            while True:
                line = input_file.readline()
                if line == "\n" or line == "":
                    break
                dst_start, src_start, range_size = (int(n) for n in line.split(" "))
                # Save maps as src_start, src_end, map_offset
                map_ranges.append([src_start, src_start + range_size, dst_start - src_start])
            # Sort map ranges based on src_start
            maps[map_name] = sorted(map_ranges)
    return seeds, maps
