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


if __name__ == "__main__":
    part_1()
