import itertools
import re

from utils import read_lines


class Program:
    MEM_RE = re.compile(r"mem\[(\d+)] = (\d+)")

    def __init__(self):
        self.instructions = read_lines(day=14)
        self.memory = {}
        self.mask = None

    def get_instruction(self):
        for i in self.instructions:
            if i.startswith("mask"):
                self.mask = i.replace("mask = ", "")
            else:
                yield re.findall(self.MEM_RE, i)[0]

    def set(self, addr, val):
        self.memory[addr] = val

    def sum_values(self):
        return sum(int(i) for i in self.memory.values())


def get_addresses(masked_address):
    addresses = []
    floating_bits = masked_address.count("X")
    options = [seq for seq in itertools.product("01", repeat=floating_bits)]

    for option in options:
        option = list(option)
        addresses.append(
            "".join(option.pop() if m == "X" else m for m in masked_address))

    return addresses


def mask_value(mask, val):
    masked = []

    for m, v in zip(mask, f"{int(val):036b}"):
        if m == "X":
            masked.append("X")
        elif m == "1" or v == "1":
            masked.append("1")
        else:
            masked.append("0")

    return masked


def part_one():
    program = Program()
    for address, val in program.get_instruction():
        masked = [v if m == "X" else m for m, v in
                  zip(program.mask, f"{int(val):036b}")]
        program.set(address, int("".join(masked), 2))

    return program.sum_values()


def part_two():
    program = Program()
    for address, val in program.get_instruction():
        masked_address = mask_value(program.mask, address)
        for masked_address in get_addresses(masked_address):
            program.set(masked_address, val)

    return program.sum_values()


assert part_one() == 9296748256641
assert part_two() == 4877695371685
