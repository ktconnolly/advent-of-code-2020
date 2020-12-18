import operator
from functools import reduce
from itertools import combinations

from utils import read_ints


def solve(n):
    for combo in combinations(read_ints(day=1), n):
        if sum(combo) == 2020:
            return reduce(operator.mul, combo, 1)


def part_one():
    return solve(2)


def part_two():
    return solve(3)


assert part_one() == 494475
assert part_two() == 267520550
