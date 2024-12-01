import sys

from collections import defaultdict

sys.path.extend([".", ".."])

from utils import *


def parse(lines) -> tuple[list[int], list[int]]:
    L, R = [], []
    for line in lines:
        l, r = line.strip().split()
        L.append(int(l))
        R.append(int(r))
    return L, R


def p1(data):
    lines = get_lines(data)
    L, R = parse(lines)

    ans = 0
    for l, r in zip(sorted(L), sorted(R)):
        ans += abs(l - r)
    return ans


def p2(data):
    lines = get_lines(data)
    L, R = parse(lines)

    count = defaultdict(int)
    for r in R:
        count[r] += 1

    ans = 0
    for l in L:
        ans += l * count.get(l, 0)
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/01.in")
    data = read_file(f"2024/ins/01.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
