def get_instructions():
    with open("inputs/day_08.txt") as file:
        return [line.strip().split() for line in file]


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
    return run(get_instructions())[0]


def part_two():
    substitutions = {"jmp": "nop", "nop": "jmp"}
    instructions = get_instructions()

    for i, (op, _) in enumerate(instructions):
        if op not in substitutions:
            continue

        instructions[i][0] = substitutions.get(op)
        accumulator, success = run(instructions)

        if success:
            return accumulator

        instructions[i][0] = op
