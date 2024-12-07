import sys

sys.path.extend([".", ".."])

from utils import *


def parse(data):
    lines = get_lines(data)
    examples = []
    for line in lines:
        segments = line.split(": ")
        ex = (int(segments[0]), list(map(int, segments[1].strip().split())))
        examples.append(ex)
    return examples


def solve(target: int, total: int, numbers: list[int], concat=False) -> int:
    if target == total and len(numbers) == 0:
        return 1
    if total > target or len(numbers) == 0:
        return 0

    num = numbers[0]
    N = solve(target, total + num, numbers[1:], concat=concat) + solve(target, total * num, numbers[1:], concat=concat)
    if concat:
        N += solve(target, int(f"{total}{num}"), numbers[1:], concat=concat)
    return N


def p1(data):
    equations = parse(data)
    ans = 0
    for target, numbers in equations:
        n = solve(target, numbers[0], numbers[1:])
        ans += target if n > 0 else 0
    return ans


def p2(data):
    equations = parse(data)
    ans = 0
    for target, numbers in equations:
        n = solve(target, numbers[0], numbers[1:], concat=True)
        ans += target if n > 0 else 0
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/07.in")
    data = read_file(f"2024/ins/07.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
