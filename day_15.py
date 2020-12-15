from collections import defaultdict, deque

from utils import read_lines


def get_input():
    numbers = [int(n) for n in read_lines(day=15, split=",")]

    history = defaultdict(lambda: deque(maxlen=2))
    for i, n in enumerate(numbers, start=1):
        history[n].append(i)

    turn = len(numbers) + 1
    curr = numbers[-1]
    return turn, curr, history


def run(limit):
    turn, curr, history = get_input()

    while turn <= limit:
        if len(history[curr]) != 2:
            curr = 0
            history[curr].append(turn)
        else:
            curr = max(history[curr]) - min(history[curr])
            history[curr].append(turn)

        turn += 1

    return curr


def part_one():
    return run(limit=2020)


def part_two():
    return run(limit=30000000)
