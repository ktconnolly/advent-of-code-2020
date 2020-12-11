import re

from utils import read_lines


def get_passports():
        return [
            {k: v for entry in line.split() for k, v in [entry.split(':')] if k != "cid"}
            for line in [lines.replace("\n", " ") for lines in read_lines(day=4, split='\n\n')]
        ]


rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: bool(re.search("1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in", x)),
    "hcl": lambda x: bool(re.search("#[a-f0-9]{6}$", x)),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: len(x) == 9 and x.isdigit()
}


def is_valid(passport):
    return all(field in passport and rule(passport[field]) for field, rule in rules.items())


def part_one():
    return sum(passport.keys() == rules.keys() for passport in get_passports())


def part_two():
    return sum(is_valid(passport) for passport in get_passports())
