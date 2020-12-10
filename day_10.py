def read_input():
    with open("inputs/day_10.txt") as file:
        return [int(line) for line in file]


def part_one():
    adapters = [0] + sorted(read_input())
    diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
    return diffs.count(1) * (diffs.count(3) + 1)


def part_two():
    adapters = sorted(read_input())

    routes = [0] * (adapters[-1] + 1)
    routes[0] = 1

    for a in adapters:
        routes[a] = routes[a - 3] + routes[a - 2] + routes[a - 1]

    return routes[-1]
