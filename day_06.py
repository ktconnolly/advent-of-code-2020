from utils import read_lines


def get_answers():
    return [line.splitlines() for line in read_lines(day=6, split="\n\n")]


def part_one():
    return sum(len(set("".join(group))) for group in get_answers())


def part_two():
    return sum(
        len(set.intersection(*map(set, group))) for group in get_answers())


assert part_one() == 6506
assert part_two() == 3243
