import itertools


def part1():
    """
    You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input).
    The filesystem consists of a tree of files and directories. The outermost directory is called /.
    Within the terminal output, lines that begin with $ are commands you executed.
    cd means change directory. This changes which directory is the current directory
        cd x moves in one level
        cd .. moves out one level
        cd / switches the current directory to the outermost directory, /.
    ls means list. It prints out all the files and directories immediately contained by the current directory:
        123 abc means that the current directory contains a file named abc with size 123.
        dir xyz means that the current directory contains a directory named xyz.
    Find the sum of all the directories with a total size of at most 100000.
    """
    program = read_input()
    root = build_filesystem(program)
    all_sizes = root.make_size_list()
    return sum(size for size in all_sizes if size <= 100000)


def part2():
    """
    The total disk space available to the filesystem is 70000000.
    To run the update, you need unused space of at least 30000000.
    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    What is the total size of that directory?
    """
    program = read_input()
    root = build_filesystem(program)
    all_sizes = root.make_size_list()

    used_space = all_sizes[-1]
    extra_free_space_needed = used_space - 40000000  # 40000000 = total filesystem size - free space required
    return min([size for size in all_sizes if size >= extra_free_space_needed])


def read_input():
    values = []
    with open('input/day7.txt') as input_file:
        for line in input_file:
            values.append(line.rstrip().split(' '))
    return values


class Node:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent: Node = parent
        self.children: dict[str, Node] = {}  # maps dir names to the Node representing it
        self.content: dict[str, int] = {}  # maps filenames to file sizes

    def make_size_list(self) -> list[int]:
        """Returns a list of the sizes of all children, with the size of this node as last entry"""
        content_size = sum(self.content.values())
        child_lists = [child.make_size_list() for child in self.children.values()]
        child_sizes = sum([child[-1] for child in child_lists])
        total_size = content_size + child_sizes
        result_list = list(itertools.chain.from_iterable(child_lists)) + [total_size]
        return result_list


def build_filesystem(program: list[list[str]]) -> Node:
    """Build the filesystem tree and return the root node"""
    root = Node('/')
    current_node = root
    for line in program:
        if line[0] == '$':
            if line[1] == 'cd':
                param = line[2]
                if param == '/':
                    # cd to filesystem root, '/'
                    current_node = root
                elif param == '..':
                    # go up one folder
                    if current_node != root:
                        current_node = current_node.parent
                else:
                    # go into a child folder
                    current_node = current_node.children[param]
            elif line[1] == 'ls':
                # No action required for the ls command
                continue
        elif line[0] == 'dir':
            # 'line' lists a child dir of the current folder
            child_name = line[1]
            if child_name not in current_node.children:
                child = Node(child_name, current_node)
                current_node.children[child_name] = child
        else:
            # 'line' lists a file in the current folder
            file_size = int(line[0])
            file_name = line[1]
            if file_name not in current_node.content:
                current_node.content[file_name] = file_size
    return root
