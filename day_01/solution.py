domain_l, domain_r = 0, 100


def day_01():
    position = 50
    zero_count = 0

    with open("input.txt", "r") as f:
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


if __name__ == "__main__":
    day_01()
