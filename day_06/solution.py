from pathlib import Path
from operator import add, mul
from functools import reduce

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"


def read_file():
    with open(input_file, "r") as f:
        for line in f:
            yield line[:-1]


def part_1():
    reader = read_file()
    problems: list[list[int | str]] = [[int(n)] for n in next(reader).split()]

    operators = {
        "+": add,
        "*": mul,
    }

    for line in reader:
        for i, val in enumerate(line.split()):
            problems[i].append(val if val in operators else int(val))

    solutions: list[int] = []
    for problem in problems:
        operator = problem.pop()
        op = add if operator == "+" else mul
        solutions.append(reduce(op, problem))

    total = reduce(add, solutions)
    print(total)


if __name__ == "__main__":
    part_1()
