import sys
import importlib


def main():
    day = 0
    part = 0
    try:
        day = int(sys.argv[1])
        part = int(sys.argv[2])
    except(IndexError, ValueError):
        print("Please enter the day number followed by the part number as first and second arguments")
        exit()

    module_name = "days.day" + str(day)
    # try:
    solver_module = importlib.import_module(module_name)

    try:
        getattr(solver_module, "part" + str(part))()
    except AttributeError:
        print("No implementation found for day", day, "part", part)
        exit()

    # except ImportError:
    #     print("No solver found for day", day)
    #     exit()


main()
