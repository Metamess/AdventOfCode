from queue import PriorityQueue


def part1():
    """
    """
    return a_star(min_path=0, max_path=3)


def part2():
    """
    """
    return a_star(min_path=4, max_path=10)


def a_star(min_path, max_path) -> int:
    grid = read_input()
    # node = j, i, length, dy, dx
    start_node = (0, 0, 0, 0, 1)
    goal = (len(grid) - 1, len(grid[0]) - 1)

    costs = {start_node: 0}
    # Queue contents: (current cost + heuristic, node)
    frontier = PriorityQueue()
    frontier.put((0, start_node))

    while not frontier.empty():
        _, node = frontier.get()
        j, i, length, dy, dx = node
        if (j, i) == goal and length >= min_path:
            return costs[node]
        new_nodes = []
        # Add going straight
        if length < max_path:
            new_nodes.append((j + dy, i + dx, length + 1, dy, dx))
        if length >= min_path or node == start_node:
            # Add going to sides
            new_nodes.append((j + dx, i + dy, 1, dx, dy))
            new_nodes.append((j - dx, i - dy, 1, -dx, -dy))

        for new_node in new_nodes:
            node_j, node_i = new_node[:2]
            if node_j < 0 or node_i < 0 or node_j == len(grid) or node_i == len(grid[0]):
                continue
            node_cost = costs[node] + grid[node_j][node_i]
            node_heuristic = (len(grid) - node_j - 1) + (len(grid[0]) - node_i - 1)
            if new_node in costs:
                if costs[new_node] > node_cost:
                    costs[new_node] = node_cost
                continue
            costs[new_node] = node_cost
            frontier.put((node_heuristic + node_cost, new_node))

    raise ValueError("Unable to find path to goal")


def read_input() -> list[list[int]]:
    with open('input/day17.txt') as input_file:
        return [[int(c) for c in line] for line in input_file.read().split()]
