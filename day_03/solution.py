from pathlib import Path

module_dir = Path(__file__).parent
input_file = f"{module_dir}/input.txt"


def part_1():
    total_joltage = 0

    with open(input_file, "r") as f:
        for line in f:
            l, r = max_pair(line.strip())
            total_joltage += int(l + r)

    print("Total:", total_joltage)


def max_pair(bank: str):
    l, r = len(bank) - 2, len(bank) - 1

    for i in range(len(bank) - 3, -1, -1):
        if bank[i] >= bank[l]:
            if bank[l] > bank[r]:
                r = l
            l = i

    return bank[l], bank[r]


if __name__ == "__main__":
    part_1()
