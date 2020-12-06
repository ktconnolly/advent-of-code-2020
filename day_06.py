def get_answers():
    with open("inputs/day_06.txt") as file:
        return [line.splitlines() for line in file.read().split("\n\n")]


def part_one():
    return sum(len(set("".join(group))) for group in get_answers())


def part_two():
    return sum(len(set.intersection(*map(set, group))) for group in get_answers())
