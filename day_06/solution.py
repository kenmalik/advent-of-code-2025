from io import StringIO
from pathlib import Path
from operator import add, mul
from functools import reduce

module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"

operators = {
    "+": add,
    "*": mul,
}


def read_lines():
    with open(input_file, "r") as f:
        for line in f:
            yield line[:-1]


def part_1():
    reader = read_lines()
    problems: list[list[int | str]] = [[int(n)] for n in next(reader).split()]

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


def part_2():
    max_widths: dict[int, int] = {}

    column_count = 0
    for line in read_lines():
        tokens = line.split()

        if tokens[0] in operators:
            column_count = len(tokens)
            break

        for i, t in enumerate(tokens):
            current = max_widths.get(i, 0)
            max_widths[i] = max(current, len(t))

    problems: list[list[str]] = [[] for _ in range(column_count)]
    for line in read_lines():
        reader = StringIO(line)

        for i, w in enumerate(max_widths.values()):
            problems[i].append(reader.read(w))
            reader.read(1)

    total = 0
    for problem in problems:
        width = len(problem[0])

        operator = problem.pop().strip()
        operands = []

        for i in reversed(range(width)):
            number = ""
            for n in problem:
                if n[i] != " ":
                    number += n[i]
            operands.append(int(number))

        total += reduce(operators[operator], operands)

    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
