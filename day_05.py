def get_boarding_passes():
    with open("inputs/day_05.txt") as file:
        return [line.strip() for line in file]


def get_half(char, lower, upper):
    mid = lower + (upper - lower) // 2
    return (lower, mid) if char in "FL" else (mid + 1, upper)


def get_seat(boarding_pass, rng):
    for i in boarding_pass:
        rng = get_half(i, *rng)
    return rng[0]


def get_seat_ids():
    ids = []
    for boarding_pass in get_boarding_passes():
        row = get_seat(boarding_pass[:7], [0, 127])
        col = get_seat(boarding_pass[7:], [0, 7])

        ids.append((row * 8) + col)

    return sorted(ids)


def part_one():
    return get_seat_ids()[-1]


def part_two():
    ids = get_seat_ids()
    return sum(range(ids[0], ids[-1] + 1)) - sum(ids)
