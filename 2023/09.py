import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def parse_lines(data):
    lines = get_lines(data)
    int_lines = []
    for line in lines:
        int_lines.append(list(map(int, line.split())))
    return int_lines


def create_diffs(line):
    return [line[i + 1] - line[i] for i in range(len(line) - 1)]


def find_next(line):
    lasts = [line[-1]]
    while not all(d == 0 for d in line):
        line = create_diffs(line)
        lasts.append(line[-1])
    return sum(lasts)


def p1(data):
    lines = parse_lines(data)
    ans = 0
    for line in lines:
        ans += find_next(line)
    return ans


def p2(data):
    # same as part 1 but reversed.
    lines = [line[::-1] for line in parse_lines(data)]
    ans = 0
    for line in lines:
        ans += find_next(line)
    return ans


if __name__ == "__main__":
    data = read_file(f"samples/09.in")
    data = read_file(f"ins/09.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
