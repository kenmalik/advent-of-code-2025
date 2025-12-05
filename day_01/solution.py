from pathlib import Path

module_dir = Path(__file__).parent
input_file = f"{module_dir}/input.txt"


domain_l, domain_r = 0, 100


def part_1():
    position = 50
    zero_count = 0

    with open(input_file, "r") as f:
        for line in f:
            direction = line[0]
            amount = int(line[1:-1])

            position = rotate(position, amount, rotate_left=direction == "L")

            if position == 0:
                zero_count += 1

    print("Password:", zero_count)


def rotate(start: int, amount: int, rotate_left: bool = False):
    position = start

    if rotate_left:
        amount = -amount

    position += amount

    if not domain_l <= position < domain_r:
        position %= domain_r

    return position


def part_2():
    position = 50
    zero_passes = 0

    with open(input_file, "r") as f:
        for line in f:
            direction = line[0]
            amount = int(line[1:-1])

            position, passes = rotate_with_passes(
                position, amount, rotate_left=direction == "L"
            )
            zero_passes += passes

    print("Password:", zero_passes)


def rotate_with_passes(start: int, amount: int, rotate_left: bool = False):
    next = start

    zero_passes = amount // domain_r
    delta = amount % domain_r

    if rotate_left:
        delta = -delta
    next += delta

    if not domain_l <= next < domain_r:
        if start != 0:
            zero_passes += 1
        next %= domain_r
    elif start != 0 and next == 0:
        zero_passes += 1

    return next, zero_passes


if __name__ == "__main__":
    part_1()
    part_2()
