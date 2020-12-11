from utils import read_lines

OCCUPIED = "#"
UNOCCUPIED = "L"
SEAT_STATES = (OCCUPIED, UNOCCUPIED)
FLOOR = "."
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


class FloorPlan:
    def __init__(self):
        self.plan = [list(line) for line in read_lines(day=11)]

    def get(self, row, cell):
        if not self.is_inbounds(row, cell):
            return None

        return self.plan[row][cell]

    def is_inbounds(self, row, col):
        return 0 <= row < len(self.plan) and 0 <= col < len(self.plan[0])

    def update(self, updates):
        for row, col, update in updates:
            self.plan[row][col] = update

    def get_visible_seats(self, row, col):
        return [
            seat
            for seat in [self.get_visible_seat(row, col, d) for d in DIRECTIONS]
            if seat is not None
        ]

    def get_visible_seat(self, row, col, direction):
        row += direction[0]
        col += direction[1]

        contents = self.get(row, col)
        while contents is not None:
            if contents in SEAT_STATES:
                return contents

            row += direction[0]
            col += direction[1]
            contents = self.get(row, col)

    def get_adjacent_seats(self, row, col):
        return [
            contents
            for contents in [self.get_adjacent(row, col, d) for d in DIRECTIONS]
            if contents in SEAT_STATES
        ]

    def get_adjacent(self, row, col, direction):
        return self.get(row + direction[0], col + direction[1])

    def get_occupied_count(self):
        return sum(row.count(OCCUPIED) for row in self.plan)

    def row_count(self):
        return len(self.plan)

    def col_count(self):
        return len(self.plan[0])


def run(part):
    floor_plan = FloorPlan()
    rows, cols = floor_plan.row_count(), floor_plan.col_count()
    tolerance = 4 if part == 1 else 5

    while True:
        updates = []

        for row in range(rows):
            for col in range(cols):

                seat = floor_plan.get(row, col)
                if seat not in SEAT_STATES:
                    continue

                if part == 1:
                    neighbours = floor_plan.get_adjacent_seats(row, col)
                else:
                    neighbours = floor_plan.get_visible_seats(row, col)

                if seat == OCCUPIED and sum(
                        seat == OCCUPIED for seat in neighbours) >= tolerance:
                    updates.append((row, col, UNOCCUPIED))
                elif seat == UNOCCUPIED and all(
                        seat == UNOCCUPIED for seat in neighbours):
                    updates.append((row, col, OCCUPIED))

        if updates:
            floor_plan.update(updates)
        else:
            return floor_plan.get_occupied_count()


def part_one():
    return run(1)


def part_two():
    return run(2)
