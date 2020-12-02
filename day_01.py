import operator
from functools import reduce
from itertools import combinations


def read_input(file):
    with open(file, "r") as f:
        return set(int(line) for line in f)


def solve(n):
    for combo in combinations(read_input("inputs/day_01.txt"), n):
        if sum(combo) == 2020:
            return reduce(operator.mul, combo, 1)


def part_one():
    return solve(2)


def part_two():
    return solve(3)
