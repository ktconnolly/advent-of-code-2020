from utils import read_ints


def find_weakness(arr, target):
    curr = 0
    while curr < target:
        for i, n in enumerate(arr):
            curr += n
            if curr == target:
                return min(arr[:i]) + max(arr[:i])


def part_one():
    xmas = read_ints(day=9)

    for i in range(25, len(xmas)):
        preamble = xmas[i - 25: i]

        if not any((xmas[i] - j) in preamble for j in preamble):
            return xmas[i]


def part_two():
    xmas = read_ints(day=9)
    target = part_one()

    for i in range(len(xmas)):
        weakness = find_weakness(xmas[i:], target)
        if weakness:
            return weakness


assert part_one() == 373803594
assert part_two() == 51152360
