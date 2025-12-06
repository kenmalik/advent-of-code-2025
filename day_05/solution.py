from __future__ import annotations
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

    def intersects(self, other: Range) -> bool:
        return (
            self.contains(other.start)
            or self.contains(other.end)
            or other.contains(self.start)
            or other.contains(self.end)
        )


def merge(a: Range, b: Range) -> Range:
    return Range(min(a.start, b.start), max(a.end, b.end))


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


def part_2():
    ranges: list[Range] = []

    for id_range in read_values():
        if id_range == "":
            break

        start, end = id_range.split("-")
        new_range = Range(int(start), int(end))

        i = 0
        while i < len(ranges):
            if new_range.intersects(ranges[i]):
                new_range = merge(new_range, ranges.pop(i))
            else:
                i += 1

        ranges.append(new_range)

    total = 0
    for r in ranges:
        total += r.end - r.start + 1

    print("Total Fresh IDs:", total)


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
    # part_1()
    part_2()
