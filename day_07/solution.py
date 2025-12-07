from pathlib import Path

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"


def line_reader():
    with open(input_file, "r") as f:
        for line in f:
            yield line.strip()


def part_1():
    reader = line_reader()
    first_line = next(reader)

    splitter = "^"
    min, max = 0, len(first_line) - 1

    beam_indices = {first_line.find("S")}

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


if __name__ == "__main__":
    part_1()
