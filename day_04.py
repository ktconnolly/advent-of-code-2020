import re
from itertools import groupby


def get_passports():
    with open("inputs/day_04.txt") as file:
        group = [list(map(str.strip, group)) for key, group in groupby(file, lambda x: x != "\n") if key]
        return [" ".join(g) for g in group]


rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: bool(re.search("1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in", x)),
    "hcl": lambda x: bool(re.search("#[a-f0-9]{6}$", x)),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: len(x) == 9 and x.isdigit()
}


def get_passport_dict(passport):
    fields = {}
    for entry in passport.split(" "):
        field, value = entry.split(":")
        if field != "cid":
            fields[field] = value

    return fields


def is_valid(passport):
    passport_dict = get_passport_dict(passport)

    for field, rule in rules.items():
        value = passport_dict.get(field)

        if value is None or not rule(value):
            return False

    return True


def part_one():
    return sum(get_passport_dict(passport).keys() == rules.keys() for passport in get_passports())


def part_two():
    return sum(is_valid(passport) for passport in get_passports())
