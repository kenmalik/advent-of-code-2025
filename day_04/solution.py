from pathlib import Path

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"

empty = "."
roll = "@"
max_adjacent = 4


def part_1():
    floor = load_floor(input_file)

    accessible = 0
    for i in range(len(floor[0])):
        for j in range(len(floor)):
            if floor[i][j] == roll and adjacent_rolls(i, j, floor) < max_adjacent:
                accessible += 1

    print(accessible)


def part_2():
    floor = load_floor(input_file)

    total_removed = 0
    while (removed := remove_accessible(floor)) > 0:
        total_removed += removed

    print(total_removed)


def remove_accessible(floor: list[list[str]]):
    accessible = 0
    for i in range(len(floor[0])):
        for j in range(len(floor)):
            if floor[i][j] == roll and adjacent_rolls(i, j, floor) < max_adjacent:
                accessible += 1
                floor[i][j] = empty

    return accessible


def load_floor(file: Path):
    floor = []
    with open(file, "r") as f:
        for line in f:
            floor.append(list(line[:-1]))
    return floor


def adjacent_rolls(i: int, j: int, floor: list[list[str]]):
    adjacent = 0

    def increment_if(condition):
        if condition:
            nonlocal adjacent
            adjacent += 1

    room_above = i > 0
    room_below = i < len(floor) - 1
    room_left = j > 0
    room_right = j < len(floor[0]) - 1

    if room_above:
        increment_if(room_left and floor[i - 1][j - 1] == roll)
        increment_if(floor[i - 1][j] == roll)
        increment_if(room_right and floor[i - 1][j + 1] == roll)

    if room_below:
        increment_if(room_left and floor[i + 1][j - 1] == roll)
        increment_if(floor[i + 1][j] == roll)
        increment_if(room_right and floor[i + 1][j + 1] == roll)

    increment_if(room_left and floor[i][j - 1] == roll)
    increment_if(room_right and floor[i][j + 1] == roll)

    return adjacent


if __name__ == "__main__":
    part_1()
    part_2()
