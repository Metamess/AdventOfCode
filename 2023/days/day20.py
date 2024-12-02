import math
from queue import Queue


def part1():
    """
    """
    nodes = read_input()
    signal_count = [0, 0]  # low, high
    for i in range(1000):
        # signal = (node_name, input_signal, sender)
        signals = Queue()
        signals.put(("broadcaster", 0, "button"))
        while not signals.empty():
            node_name, input_signal, sender = signals.get()
            signal_count[input_signal] += 1
            variant, state, outputs = nodes[node_name]
            if variant == "broadcaster":
                out_signal = input_signal
            elif variant == "flipflop":
                if input_signal == 1:
                    continue
                out_signal = 1 - state
                nodes[node_name] = (variant, out_signal, outputs)
            elif variant == "conjunction":
                state[sender] = input_signal
                nodes[node_name] = (variant, state, outputs)
                if all(s == 1 for s in state.values()):
                    out_signal = 0
                else:
                    out_signal = 1
            else:
                assert variant == "null"
                continue
            for output_node in outputs:
                signals.put((output_node, out_signal, node_name))
    return signal_count[0] * signal_count[1]


def part2():
    """
    """
    # node = (variant, state, outputs)
    nodes = read_input()
    conjunctions = {name: state.copy() for name, (variant, state, outputs) in nodes.items() if variant == "conjunction"}
    button_presses = 0
    while True:
        # signal = (node_name, input_signal, sender)
        signals = Queue()
        signals.put(("broadcaster", 0, "button"))
        button_presses += 1
        rx_inputs = []
        while not signals.empty():
            node_name, input_signal, sender = signals.get()
            variant, state, outputs = nodes[node_name]
            if variant == "broadcaster":
                out_signal = input_signal
            elif variant == "flipflop":
                if input_signal == 1:
                    continue
                out_signal = 1 - state
                nodes[node_name] = (variant, out_signal, outputs)
            elif variant == "conjunction":
                state[sender] = input_signal
                if input_signal == 1 and conjunctions[node_name][sender] == 0:
                    conjunctions[node_name][sender] = button_presses
                    if any(nodes[output][0] == "null" for output in outputs) and all(s != 0 for s in conjunctions[node_name].values()):
                        return math.lcm(*list(conjunctions[node_name].values()))
                nodes[node_name] = (variant, state, outputs)
                if all(s == 1 for s in state.values()):
                    out_signal = 0
                else:
                    out_signal = 1
            else:
                assert variant == "null"
                rx_inputs.append(input_signal)
                continue
            for output_node in outputs:
                signals.put((output_node, out_signal, node_name))
        if rx_inputs == [0]:
            return button_presses


def read_input():
    # node = (variant, state, outputs)
    nodes: dict[str, tuple[str, int | dict[str, int], list[str]]] = {}
    with open('input/day20.txt') as input_file:
        for line in input_file:
            node_str, outputs = line.rstrip().split(' -> ')
            outputs = outputs.split(', ')
            if node_str[0] == '%':
                # flipflop: toggles on low pulses, sends low if turned off and high if turned on
                nodes[node_str[1:]] = ("flipflop",  0, outputs)
            elif node_str[0] == '&':
                # conjunction: if all inputs high: send low, else high
                nodes[node_str[1:]] = ("conjunction", {}, outputs)
            else:
                assert node_str == "broadcaster"
                nodes[node_str] = ("broadcaster", 0, outputs)

    # initialize conjunction nodes
    null_nodes = {}
    for node_name, (variant, state, outputs) in nodes.items():
        for output in outputs:
            if output not in nodes:
                assert output == "rx"
                null_nodes[output] = ("null", 0, [])
            elif nodes[output][0] == "conjunction":
                nodes[output][1][node_name] = 0
    nodes.update(null_nodes)
    return nodes
