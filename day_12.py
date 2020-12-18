from utils import read_lines

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

MOVES = {
    LEFT: {
        NORTH: WEST,
        EAST: NORTH,
        SOUTH: EAST,
        WEST: SOUTH
    },
    RIGHT: {
        NORTH: EAST,
        EAST: SOUTH,
        SOUTH: WEST,
        WEST: NORTH
    }
}


def move(coords, direction, units):
    if direction == NORTH:
        coords[1] += units
    elif direction == SOUTH:
        coords[1] -= units
    elif direction == EAST:
        coords[0] += units
    elif direction == WEST:
        coords[0] -= units


def part_one():
    current_direction = EAST
    ship = [0, 0]
    for instruction in read_lines(day=12):
        action, units = instruction[:1], int(instruction[1:])

        if action in (NORTH, EAST, SOUTH, WEST):
            move(ship, action, units)
        elif action == FORWARD:
            move(ship, current_direction, units)
        elif action in (LEFT, RIGHT):
            for i in range(units // 90):
                current_direction = MOVES[action][current_direction]

    return abs(ship[0]) + abs(ship[1])


def part_two():
    ship = [0, 0]
    waypoint = [10, 1]
    for instruction in read_lines(day=12):
        action, units = instruction[:1], int(instruction[1:])

        if action == FORWARD:
            ship[0] += units * waypoint[0]
            ship[1] += units * waypoint[1]
        elif action in (NORTH, EAST, SOUTH, WEST):
            move(waypoint, action, units)
        elif action in (LEFT, RIGHT):
            for i in range(units // 90):
                if action == RIGHT:
                    waypoint = [waypoint[1], -waypoint[0]]
                elif action == LEFT:
                    waypoint = [-waypoint[1], waypoint[0]]

    return abs(ship[0]) + abs(ship[1])


assert part_one() == 1710
assert part_two() == 62045
