import re
from abc import ABC

from utils import read_lines

TERMINAL_PATTERN = re.compile("([a-zA-z])")


class Result:
    """
    Represents how many characters we wanted to match vs how many were
    actually matched by a rule
    """

    def __init__(self, got=0, wanted=0):
        self.got = got
        self.wanted = wanted

    def update(self, result):
        self.got += result.got
        self.wanted += result.wanted

    def __bool__(self):
        return self.got == self.wanted

    def __repr__(self):
        return f"got={self.got}, wanted={self.wanted}"


class Rule(ABC):
    def matches(self, candidate):
        pass


class TerminalRule(Rule):
    def __init__(self, to_match):
        self.to_match = to_match

    def matches(self, candidate):
        if self.to_match == candidate[0]:
            return Result(got=1, wanted=1)
        return Result(got=0, wanted=1)

    def __repr__(self):
        return f"to_match=='{self.to_match}'"


class CompoundRule(Rule):
    def __init__(self, rules):
        self.rules = rules

    def matches(self, candidate):
        overall_result = Result()

        for rule in self.rules:
            result = rule.matches(candidate)
            overall_result.update(result)

            if result:
                candidate = candidate[result.got:]
            else:
                # short circuit if not successful
                return overall_result

        return overall_result

    def __repr__(self):
        return f"{' AND '.join(self.rules)}"


class OrRule(Rule):
    def __init__(self, left: Rule, right: Rule):
        self.left = left
        self.right = right

    def matches(self, candidate):
        return self.left.matches(candidate) or self.right.matches(candidate)

    def __repr__(self):
        return f"[{self.left} or {self.right}]"


def parse_rule(rule, rules_map):
    if match := TERMINAL_PATTERN.search(rule):
        return TerminalRule(match.group())

    if rule.isdigit():
        return parse_rule(rules_map.get(rule), rules_map)

    if " | " in rule:
        left, right = rule.split(" | ")
        return OrRule(parse_rule(left, rules_map),
                      parse_rule(right, rules_map))

    if " " in rule:
        rules = [parse_rule(rules_map.get(rule), rules_map) for rule in
                 rule.split(" ")]
        return CompoundRule(rules)


def part_one():
    rules, messages = read_lines(day=19, split="\n\n")
    rules, messages = rules.split("\n"), messages.split("\n")

    rules_map = {}
    for rule in rules:
        number, rule = rule.split(": ")
        rules_map[number] = rule

    rules = parse_rule(rules_map["0"], rules_map)

    matches = []
    for msg in messages:
        result = rules.matches(msg)
        # check length of message to prevent partial matches
        if result and result.got == len(msg):
            matches.append(msg)

    return len(matches)


assert part_one() == 205
