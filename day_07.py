import re
from collections import defaultdict

from utils import read_lines


def get_rules():
    child_to_parent = defaultdict(set)
    parent_to_child = defaultdict(set)
    for rule in read_lines(day=7):
        parent = re.match(r"(^\w+ \w+)", rule)[1]

        for quantity, child in re.findall(r"(\d+) (\w+ \w+)", rule):
            child_to_parent[child].add(parent)
            parent_to_child[parent].add((int(quantity), child))

    return child_to_parent, parent_to_child


def part_one():
    def get_parents(child, child_to_parent):
        parents = set()
        for parent in child_to_parent[child]:
            parents.add(parent)
            parents.update(get_parents(parent, child_to_parent))

        return parents

    rules, _ = get_rules()
    return len(get_parents("shiny gold", rules))


def part_two():
    def get_total(parent, parent_to_child):
        return sum(
            quantity + (quantity * get_total(child, parent_to_child)) for
            quantity, child in parent_to_child[parent])

    _, rules = get_rules()
    return get_total("shiny gold", rules)


assert part_one() == 179
assert part_two() == 18925
