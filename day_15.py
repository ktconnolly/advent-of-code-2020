from utils import read_lines


def run(limit):
    numbers = [int(n) for n in read_lines(day=15, split=",")]
    history = {n: i for i, n in enumerate(numbers[:-1], start=1)}
    prev_num = numbers[-1]

    for turn in range(len(numbers), limit):
        next_num = turn - history.get(prev_num, turn)
        history[prev_num] = turn
        prev_num = next_num

    return prev_num


def part_one():
    return run(limit=2020)


def part_two():
    return run(limit=30000000)


assert part_one() == 206
assert part_two() == 955
