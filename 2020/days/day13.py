import math


def part1():
    """
    Each bus has an ID number that also indicates how often the bus leaves for the airport.
    Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past.
    Your notes (your puzzle input) consist of two lines.
    The first line is your estimate of the earliest timestamp you could depart on a bus.
    The second line lists the bus IDs that are in service according to the shuttle company;
    entries that show x must be out of service, so you decide to ignore them.
    What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
    """
    my_arrival_time, buses = read_input()
    buses = [int(i) for i in buses if i != 'x']
    bus_arrival_times = [math.ceil(my_arrival_time/bus)*bus for bus in buses]
    next_arrival = min(bus_arrival_times)
    next_bus = buses[bus_arrival_times.index(next_arrival)]
    print(next_bus * (next_arrival - my_arrival_time))


def part2():
    """

    """
    _, buses = read_input()
    buses = ['x' if i == 'x' else int(i) for i in buses]
    offsets = {bus_id: -i % bus_id for i, bus_id in enumerate(buses) if bus_id != 'x'}
    print(offsets)
    time = 0
    lcm = 1
    for bus in offsets:
        while time % bus != offsets[bus]:
            time += lcm
        lcm *= bus
    print(time)


def read_input():
    with open('input/day13.txt') as input_file:
        my_arrival_time = int(input_file.readline())
        buses = input_file.readline().rstrip().split(',')
        return my_arrival_time, buses
