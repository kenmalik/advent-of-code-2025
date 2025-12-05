from pathlib import Path

module_dir = Path(__file__).parent
input_file = f"{module_dir}/input.txt"


def part_1():
    total = 0
    for r in read_ranges():
        start, end = (int(val) for val in r.split("-"))
        print(start, end)
        for i in range(start, end + 1):
            if has_repeat(str(i)):
                print(f"  {i}")
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


def has_repeat(s: str):
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[0:mid] == s[mid:]


if __name__ == "__main__":
    part_1()
