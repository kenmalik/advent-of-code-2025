import argparse

parser = argparse.ArgumentParser(
    prog="AOC2025",
    description="Run solutions for Advent of Code 2025",
)

parser.add_argument("day")


def main():
    args = parser.parse_args()
    print(f"Day {args.day} Solution:")


if __name__ == "__main__":
    main()
