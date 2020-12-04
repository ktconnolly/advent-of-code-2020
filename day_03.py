import operator
from functools import reduce


def get_map():
    with open("inputs/day_03.txt") as file:
        return [line.strip() for line in file]


def traverse_map(tree_map, slope):
    width, height = len(tree_map[0]), len(tree_map)
    row, col, trees = 0, 0, 0

    while row < height:
        if tree_map[row][col] == "#":
            trees += 1

        row += slope[0]
        col = (col + slope[1]) % width

    return trees


def part_one():
    return traverse_map(get_map(), (1, 3))


def part_two():
    tree_map = get_map()
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    return reduce(operator.mul, (traverse_map(tree_map, slope) for slope in slopes), 1)
