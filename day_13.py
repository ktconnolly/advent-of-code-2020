from utils import read_lines


def part_one():
    earliest, buses = read_lines(day=13)
    earliest = int(earliest)
    buses = [int(t) for t in buses.split(",") if t != "x"]

    current = earliest
    while True:
        for time in buses:
            if current % time == 0:
                return (current - earliest) * time

        current += 1


def part_two():
    _, times = read_lines(day=13)
    times = [(i, int(t)) for i, t in enumerate(times.split(',')) if t != "x"]

    pos = increment = times[0][1]
    for offset, time in times[1:]:
        while (pos + offset) % time != 0:
            pos += increment

        increment *= time

    return pos
