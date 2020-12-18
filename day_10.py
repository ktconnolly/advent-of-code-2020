from utils import read_ints


def part_one():
    adapters = [0] + sorted(read_ints(day=10))
    diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
    return diffs.count(1) * (diffs.count(3) + 1)


def part_two():
    adapters = sorted(read_ints(day=10))

    routes = [0] * (adapters[-1] + 1)
    routes[0] = 1

    for a in adapters:
        routes[a] = routes[a - 3] + routes[a - 2] + routes[a - 1]

    return routes[-1]


assert part_one() == 2176
assert part_two() == 18512297918464
