def read_ints(day):
    with open(f"inputs/day_{day:02d}.txt") as file:
        return [int(line) for line in file]


def read_lines(day, split=None):
    with open(f"inputs/day_{day:02d}.txt") as file:
        if split is None:
            return [line.strip() for line in file]
        return [line.strip() for line in file.read().split(split)]


def flatten_list(to_flatten):
    return [item for sublist in to_flatten for item in sublist]
