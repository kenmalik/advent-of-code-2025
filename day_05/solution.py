from pathlib import Path
from dataclasses import dataclass

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"


@dataclass
class Range:
    start: int
    end: int

    def contains(self, val: int):
        return self.start <= val <= self.end


def part_1():
    ranges: list[Range] = []

    reading_ranges = True

    fresh_count = 0

    for value in read_values():
        if value == "":
            reading_ranges = False
            continue

        if reading_ranges:
            start, end = (int(x) for x in value.split("-"))
            ranges.append(Range(start, end))
        else:
            if is_fresh(int(value), ranges):
                fresh_count += 1

    print(fresh_count)


def is_fresh(val: int, ranges: list[Range]):
    for r in ranges:
        if r.contains(val):
            return True
    return False


def read_values():
    with open(input_file, "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    part_1()
