from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"


def part_1():
    points = read_points(input_file)

    max_area = rect_area(points[0], points[1])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            max_area = max(rect_area(points[i], points[j]), max_area)

    print(max_area)


def rect_area(p1: Point, p2: Point):
    width = abs(p1.x - p2.x) + 1
    height = abs(p1.y - p2.y) + 1
    return width * height


def read_points(file: Path) -> list[Point]:
    points: list[Point] = []
    with open(file, "r") as f:
        for line in f:
            p = (int(d) for d in line.strip().split(","))
            points.append(Point(*p))

    return points


def part_2():
    x_sorted = sorted(read_points(input_file), key=lambda p: p.x)
    y_sorted = sorted(x_sorted, key=lambda p: p.y)

    def is_valid(p1: Point, p2: Point):
        if p1.x == p2.x or p1.y == p2.y:
            return True

        p1x_idx = binary_search(p1.x, x_sorted, lambda p: p.x)
        p1y_idx = binary_search(p1.y, y_sorted, lambda p: p.y)

        p2x_idx = binary_search(p2.x, x_sorted, lambda p: p.x)
        p2y_idx = binary_search(p2.y, y_sorted, lambda p: p.y)

        if abs(p1x_idx - p2x_idx) > 1 or abs(p1y_idx - p2y_idx) > 1:
            return False

        return True

    max_area = rect_area(x_sorted[0], x_sorted[1])
    for i in range(len(x_sorted)):
        for j in range(i + 1, len(x_sorted)):
            p1, p2 = x_sorted[i], x_sorted[j]
            if is_valid(p1, p2):
                print(p1, p2)
                max_area = max(rect_area(x_sorted[i], x_sorted[j]), max_area)

    print(max_area)


def binary_search(val, c, key):
    l, r = 0, len(c) - 1

    while l <= r:
        mid = (l + r) // 2
        if key(c[mid]) == val:
            return mid
        elif key(c[mid]) < val:
            r = mid - 1
        else:
            l = mid + 1

    return -1


if __name__ == "__main__":
    # part_1()
    part_2()
