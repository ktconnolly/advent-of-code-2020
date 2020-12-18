import operator
import re
from functools import reduce

from utils import read_lines, flatten_list

RANGE_PATTERN = re.compile(r"(\d+-\d+)")


def parse_fields(fields_list):
    def get_range(s):
        # Converts a string '36-626' into range(36, 627)
        lower, upper = s.split("-")
        return range(int(lower), int(upper) + 1)

    field_name_to_ranges = {}
    for field in fields_list.split("\n"):
        name, _ = field.split(": ")
        field_name_to_ranges[name] = [get_range(rng) for rng in RANGE_PATTERN.findall(field)]

    return field_name_to_ranges


def parse_ticket(ticket):
    return [int(s) for s in ticket.split(",")]


def get_input():
    fields, my_ticket, nearby_tickets = read_lines(day=16, split="\n\n")

    fields = parse_fields(fields)
    my_ticket = parse_ticket(my_ticket.split("\n")[1])
    nearby_tickets = [parse_ticket(t) for t in nearby_tickets.split("\n")[1:]]

    return fields, my_ticket, nearby_tickets


def is_entry_valid_for_any_field(entry, fields):
    ranges = fields.values()
    return any(entry in rng[0] or entry in rng[1] for rng in ranges)


def get_invalid_entries(ticket, fields):
    return [entry for entry in ticket if not is_entry_valid_for_any_field(entry, fields)]


def are_all_entries_valid_for_field(ranges, entries):
    return all(entry in ranges[0] or entry in ranges[1] for entry in entries)


def get_fields_for_entry(fields, entries):
    # Returns all field names with ranges that satisfy all given ticket entries
    return [name for name, ranges in fields.items() if are_all_entries_valid_for_field(ranges, entries)]


def is_valid(ticket, fields):
    return not get_invalid_entries(ticket, fields)


def get_valid_tickets(tickets, fields):
    return [ticket for ticket in tickets if is_valid(ticket, fields)]


def get_departure_indexes(fields_array):
    return [i for i, field in enumerate(fields_array) if field.startswith("departure")]


def part_one():
    fields, _, nearby_tickets = get_input()
    invalid_entries = [get_invalid_entries(ticket, fields) for ticket in nearby_tickets]
    return sum(flatten_list(invalid_entries))


def part_two():
    fields, my_ticket, nearby_tickets = get_input()

    valid_tickets = get_valid_tickets(nearby_tickets, fields)

    known_fields = [None] * len(valid_tickets[0])
    unknown_fields = [set(get_fields_for_entry(fields, entries)) for entries in (zip(*valid_tickets))]

    while any(field is None for field in known_fields):
        for i, candidates in enumerate(unknown_fields):
            if len(candidates) == 1:
                known_fields[i] = candidates.pop()

            unknown_fields[i] = unknown_fields[i] - set(known_fields)

    departure_entries = [my_ticket[i] for i in get_departure_indexes(known_fields)]

    return reduce(operator.mul, departure_entries, 1)


assert part_one() == 30869
assert part_two() == 4381476149273
