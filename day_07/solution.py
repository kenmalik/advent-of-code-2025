from collections import defaultdict
from functools import reduce
from operator import add
from pathlib import Path

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"

source = "S"
splitter = "^"


def line_reader():
    with open(input_file, "r") as f:
        for line in f:
            yield line.strip()


def part_1():
    reader = line_reader()
    first_line = next(reader)

    min, max = 0, len(first_line) - 1

    beam_indices = {first_line.find(source)}

    split_count = 0
    for line in reader:
        to_add = set()
        to_remove = set()

        for i in beam_indices:
            if line[i] == splitter:
                if i + 1 <= max:
                    to_add.add(i + 1)
                if i - 1 >= min:
                    to_add.add(i - 1)
                to_remove.add(i)
                split_count += 1

        beam_indices.update(to_add)
        beam_indices.difference_update(to_remove)

    print(split_count)


def part_2():
    reader = line_reader()
    first_line = next(reader)

    min, max = 0, len(first_line) - 1

    beam_indices = defaultdict(int)
    beam_indices[first_line.find(source)] = 1

    for line in reader:
        to_add = defaultdict(int)
        to_delete = set()

        for i, source_timelines in beam_indices.items():
            if line[i] == splitter:
                if i + 1 <= max:
                    to_add[i + 1] += source_timelines
                if i - 1 >= min:
                    to_add[i - 1] += source_timelines
                to_delete.add(i)

        for i, source_timelines in to_add.items():
            beam_indices[i] += source_timelines

        for i in to_delete:
            del beam_indices[i]

    total_timelines = reduce(add, beam_indices.values())
    print(total_timelines)


if __name__ == "__main__":
    part_1()
    part_2()
