import re


def get_rules():
    def get_lines():
        with open("inputs/day_07.txt") as file:
            return file.readlines()

    rules = {}
    for rule in get_lines():
        bag = re.search(r"(^\w+ \w+)", rule).group(0).strip()
        children = re.findall(r"(\d+ \w+ \w+)", rule)

        rules[bag] = []
        for child in children:
            quantity = int(child[0])
            child = [child[2:]]
            rules[bag] += child * quantity

    return rules


def contains_gold(bag, rules, cache):
    if bag in cache:
        return cache[bag]

    for child in rules.get(bag):
        if child == "shiny gold" or contains_gold(child, rules, cache):
            cache[child] = True
            return True

    cache[bag] = False
    return False


def part_one():
    rules = get_rules()
    return sum(contains_gold(bag, rules, cache={}) for bag in rules)


def part_two():
    def count_children(bag, rules):
        children = rules.get(bag)
        return sum(
            count_children(child, rules) for child in children) + len(
            children)

    return count_children("shiny gold", get_rules())
