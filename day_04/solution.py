from pathlib import Path

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"

roll = "@"
max_adjacent = 4


def part_1():
    floor = []

    with open(input_file, "r") as f:
        for line in f:
            floor.append(list(line[:-1]))

    x_max = len(floor[0])
    y_max = len(floor)

    def adjacent_rolls(i: int, j: int):
        adjacent = 0

        def increment_if(condition):
            if condition:
                nonlocal adjacent
                adjacent += 1

        room_above = i > 0
        room_below = i < y_max - 1
        room_left = j > 0
        room_right = j < x_max - 1

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

    accessible = 0
    for i in range(y_max):
        for j in range(x_max):
            if floor[i][j] == roll and adjacent_rolls(i, j) < max_adjacent:
                accessible += 1

    print(accessible)


if __name__ == "__main__":
    part_1()
