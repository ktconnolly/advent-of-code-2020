import operator
from collections import Counter
from itertools import product

from utils import read_lines


def get_active(dimensions):
    cubes = set()
    for y, row in enumerate(read_lines(day=17)):
        for x, cube in enumerate(row):
            if cube == "#":
                cubes.add(tuple([y, x] + [0 for _ in range(dimensions - 2)]))
    return cubes


def get_neighbours(cube, dimensions):
    for neighbour in product((-1, 0, 1), repeat=dimensions):
        # Need to skip all 0s
        if any(neighbour):
            yield tuple(map(operator.add, cube, neighbour))


def get_active_neighbours_map(active, dimensions):
    active_neighbours = Counter()
    for cube in active:
        for neighbour in get_neighbours(cube, dimensions):
            active_neighbours[neighbour] += 1

    return active_neighbours


def cycle(active, dimensions):
    active_neighbours = get_active_neighbours_map(active, dimensions)

    active = [cube for cube in active if active_neighbours[cube] in (2, 3)]

    to_activate = [cube for cube, active_neighbours in active_neighbours.items()
                   if cube not in active and active_neighbours == 3]

    return set(active) | set(to_activate)


def part_one():
    dimensions = 3
    cubes = get_active(dimensions)
    for _ in range(6):
        cubes = cycle(cubes, dimensions)

    return len(cubes)


def part_two():
    dimensions = 4
    cubes = get_active(dimensions)
    for _ in range(6):
        cubes = cycle(cubes, dimensions)

    return len(cubes)
