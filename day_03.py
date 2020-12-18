import operator
from functools import reduce

from utils import read_lines


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
    return traverse_map(read_lines(day=3), (1, 3))


def part_two():
    tree_map = read_lines(3)
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    return reduce(operator.mul,
                  (traverse_map(tree_map, slope) for slope in slopes), 1)


assert part_one() == 216
assert part_two() == 6708199680
