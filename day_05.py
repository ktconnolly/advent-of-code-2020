from utils import read_lines


def get_half(char, lower, upper):
    mid = lower + (upper - lower) // 2
    return (lower, mid) if char in "FL" else (mid + 1, upper)


def get_seat(boarding_pass, rng):
    for i in boarding_pass:
        rng = get_half(i, *rng)
    return rng[0]


def get_seat_ids():
    ids = []
    for boarding_pass in read_lines(day=5):
        row = get_seat(boarding_pass[:7], [0, 127])
        col = get_seat(boarding_pass[7:], [0, 7])

        ids.append((row * 8) + col)

    return ids


def part_one():
    return max(get_seat_ids())


def part_two():
    ids = get_seat_ids()
    return sum(range(min(ids), max(ids) + 1)) - sum(ids)


assert part_one() == 951
assert part_two() == 653
