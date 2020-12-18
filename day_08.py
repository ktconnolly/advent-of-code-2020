from utils import read_lines


def run(instructions):
    accumulator, pc = 0, 0
    history = set()

    while pc not in history and pc < len(instructions):
        history.add(pc)

        op, arg = instructions[pc]

        if op == "acc":
            accumulator += int(arg)
            pc += 1
        elif op == "jmp":
            pc += int(arg)
        else:
            pc += 1

    return accumulator, pc >= len(instructions)


def part_one():
    instructions = [line.split() for line in read_lines(day=8)]
    return run(instructions)[0]


def part_two():
    substitutions = {"jmp": "nop", "nop": "jmp"}
    instructions = [line.split() for line in read_lines(day=8)]

    for i, (op, _) in enumerate(instructions):
        if op not in substitutions:
            continue

        instructions[i][0] = substitutions.get(op)
        accumulator, success = run(instructions)

        if success:
            return accumulator

        instructions[i][0] = op


assert part_one() == 1548
assert part_two() == 1375
