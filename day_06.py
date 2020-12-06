def get_answers():
    with open("inputs/day_06.txt") as file:
        return file.read().split("\n\n")


def part_one():
    return sum(len(set("".join(group.replace("\n", "")))) for group in get_answers())


def part_two():
    return sum(len(set.intersection(*map(set, group.split("\n")))) for group in get_answers())
