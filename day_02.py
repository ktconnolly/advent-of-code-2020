import re


def parse_policy(line):
    match = re.search("(\d+)-(\d+) ([a-zA-Z]): (.*)", line)
    return match.group(1), match.group(2), match.group(3), match.group(4)


def is_valid_part_one(line):
    minimum, maximum, char, password = parse_policy(line)
    return int(minimum) <= password.count(char) <= int(maximum)


def is_valid_part_two(line):
    pos_1, pos_2, char, password = parse_policy(line)
    return (password[int(pos_1) - 1] == char) != (password[int(pos_2) - 1] == char)


def part_one():
    with open("inputs/day_02.txt", "r") as f:
        return sum(is_valid_part_one(l.strip()) for l in f)


def part_two():
    with open("inputs/day_02.txt", "r") as f:
        return sum(is_valid_part_two(l.strip()) for l in f)
