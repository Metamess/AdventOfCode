from copy import deepcopy


def part1():
    """
    """
    blocks = read_input()
    supports, leans_on = settle_blocks(blocks)
    # for b, o in supports.items():
    #     print(f"{chr(ord('A') + b)} {b} supports {o}")
    # print()
    # for b, o in leans_on.items():
    #     print(f"{b} leans on {o}")
    return len([b for b in range(len(blocks)) if not any(len(leans_on[o]) == 1 for o in supports.get(b, []))])


def settle_blocks(blocks):
    blocks.sort(key=lambda x: x[-1])  # sort by lowest point
    blocks_by_height = {0: [(-1, min(b[0] for b in blocks), min(b[1] for b in blocks), 0, max(b[3] for b in blocks),
                             max(b[4] for b in blocks), 0)]}
    supports = {-1: [-1]}
    leans_on = {-1: [-1]}
    # for i, block in enumerate(blocks):
    #     print(f"{i}: {block}")
    # print()
    for i, block in enumerate(blocks):
        # print(f"Checking block {i}: {block}")
        x1, y1, z1, x2, y2, z2 = block
        leans_on[i] = []
        for check_z in reversed(range(z1)):
            if check_z not in blocks_by_height:
                # print(f"  Skipping {check_z}, no blocks end there")
                continue

            for other in blocks_by_height[check_z]:
                oid, ox1, oy1, oz1, ox2, oy2, oz2 = other
                if (ox1 <= x1 <= ox2 or ox1 <= x2 <= ox2 or x1 <= ox1 <= ox2 <= x2) and (
                        oy1 <= y1 <= oy2 or oy1 <= y2 <= oy2 or y1 <= oy1 <= oy2 <= y2):
                    leans_on[i].append(oid)
                    supports.setdefault(oid, []).append(i)
            if not leans_on[i]:
                # print(f"  No collision found for block {i} at height {check_z}")
                continue
            # print(f"  Brick {i} leans on {leans_on[i]}")
            dz = z2 - z1
            z1 = check_z + 1
            z2 = z1 + dz
            # blocks[i] = (x1, y1, z1, x2, y2, z2)
            blocks_by_height.setdefault(z2, []).append((i, x1, y1, z1, x2, y2, z2))
            break
        else:
            raise ValueError(f"No ground found for block {i}, {block}")
    return supports, leans_on


def part2():
    """
    """
    blocks = read_input()
    supports, leans_on = settle_blocks(blocks)
    total = 0
    for i in range(len(blocks)):
        # print(f"Checking block {i}")
        i_total = -1
        supports_copy = deepcopy(supports)
        leans_on_copy = deepcopy(leans_on)
        pop_list = [i]
        while pop_list:
            popping = pop_list.pop()
            # if i != popping:
            #     print(f"  Block {i} causes block {popping} to pop")
            i_total += 1
            for other in supports_copy.get(popping, []):
                leans_on_copy[other].remove(popping)
                if len(leans_on_copy[other]) == 0:
                    pop_list.append(other)
        # if i_total:
        #     print(f"Block {i} causes a total of {i_total} other blocks to pop")
        total += i_total
    return total


def read_input() -> list[tuple[int, ...]]:
    blocks = []
    with open('input/day22.txt') as input_file:
        for line in input_file:
            start, end = line.rstrip().split('~')
            blocks.append(tuple(int(x) for x in [*start.split(','), *end.split(',')]))
    return blocks
