from pathlib import Path
from functools import partial

module_dir = Path(__file__).parent
input_file = f"{module_dir}/input.txt"


def part_1():
    total_joltage(max_pair)


def part_2():
    batteries_per_bank = 12
    total_joltage(partial(max_n, battery_count=batteries_per_bank))


def total_joltage(selector):
    total_joltage = 0

    with open(input_file, "r") as f:
        for line in f:
            bank_max = selector(line.strip())
            print(line, end="")
            print(f"  {bank_max}")
            total_joltage += bank_max

    print("Total:", total_joltage)


def max_pair(bank: str):
    l, r = len(bank) - 2, len(bank) - 1

    for i in range(len(bank) - 3, -1, -1):
        if bank[i] >= bank[l]:
            if bank[l] > bank[r]:
                r = l
            l = i

    return int(bank[l] + bank[r])


def max_n(bank: str, battery_count: int):
    ptrs = list(range(len(bank) - battery_count, len(bank)))

    def shift(to: int, ptr_index: int):
        if ptr_index == len(ptrs) - 1:
            ptrs[ptr_index] = to
            return

        current = ptrs[ptr_index]
        next = ptrs[ptr_index + 1]

        if bank[current] >= bank[next]:
            shift(current, ptr_index + 1)

        ptrs[ptr_index] = to

    for i in range(len(bank) - battery_count - 1, -1, -1):
        if bank[i] >= bank[ptrs[0]]:
            shift(i, 0)

    return int("".join(bank[i] for i in ptrs))


if __name__ == "__main__":
    part_1()
    part_2()
