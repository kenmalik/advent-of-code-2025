from functools import reduce
from operator import mul
from pathlib import Path
from dataclasses import dataclass
from heapq import heappush_max, heappushpop_max, heappush, heappushpop


module_dir = Path(__file__).parent
input_file = module_dir / "input.txt"


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int


def part_1():
    largest_heap: list[int] = []
    n = 3

    points = read_points(input_file)
    closest = closest_pairs(points, n=1000)

    for c in circuits(closest):
        if len(largest_heap) < n:
            heappush(largest_heap, len(c))
        else:
            heappushpop(largest_heap, len(c))

    product = reduce(mul, largest_heap)
    print(product)


def circuits(pairs: list[tuple[Point, Point]]) -> list[set[Point]]:
    circuits: list[set[Point]] = []
    for p1, p2 in pairs:
        connections = []

        for i in range(len(circuits) - 1, -1, -1):
            c = circuits[i]
            if p1 in c or p2 in c:
                connections.append(circuits.pop(i))

        new_circuit = {p1, p2}
        for c in connections:
            new_circuit |= c
        circuits.append(new_circuit)

    return circuits


def closest_pairs(points: list[Point], n: int = 10) -> list[tuple[Point, Point]]:
    closest_heap = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist2(points[i], points[j])
            if len(closest_heap) < n:
                heappush_max(closest_heap, (d, i, j))
            else:
                heappushpop_max(closest_heap, (d, i, j))

    return [(points[i], points[j]) for _, i, j in closest_heap]


def read_points(file: Path) -> list[Point]:
    points: list[Point] = []
    with open(file, "r") as f:
        for line in f:
            point = (int(d) for d in line.strip().split(","))
            points.append(Point(*point))

    return points


def dist2(a: Point, b: Point) -> int:
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z

    return dx * dx + dy * dy + dz * dz


if __name__ == "__main__":
    part_1()
