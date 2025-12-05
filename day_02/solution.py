from pathlib import Path

module_dir = Path(__file__).parent
input_file = f"{module_dir}/input.txt"


def part_1():
    check_ranges(has_double_repeat)


def part_2():
    check_ranges(has_repeats)


def check_ranges(check):
    total = 0
    for r in read_ranges():
        start, end = (int(val) for val in r.split("-"))
        for i in range(start, end + 1):
            if check(str(i)):
                total += i

    print("Total:", total)


def read_ranges():
    with open(input_file, "r") as f:
        r = ""
        while True:
            c = f.read(1)
            if not c:
                yield r
                break
            elif c == ",":
                yield r
                r = ""
            else:
                r += c


def has_double_repeat(s: str):
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[0:mid] == s[mid:]


def has_repeats(s: str):
    for divisor in range(len(s), 1, -1):
        if len(s) % divisor != 0:
            continue
        pattern_length = len(s) // divisor
        if has_repeating_pattern(s, pattern_length):
            return True

    return False


def has_repeating_pattern(s: str, pattern_length: int):
    pattern = s[0:pattern_length]
    for start in range(pattern_length, len(s), pattern_length):
        segment = s[start : start + pattern_length]
        if segment != pattern:
            return False
    return True


if __name__ == "__main__":
    part_1()
    part_2()
