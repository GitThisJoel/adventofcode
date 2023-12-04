import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def parse_line(line):
    _, numbers = line.split(": ")
    win, our = numbers.split(" | ")
    win = set(map(int, win.split()))
    our = set(map(int, our.split()))
    return win, our


def p1(data):
    lines = get_lines(data)
    ans = 0
    for line in lines:
        win, our = parse_line(line)
        w = len(win & our)
        if w > 0:
            ans += 2 ** (w - 1)
    return ans


def p2(data):
    lines = get_lines(data)
    counts = [1] * len(lines)
    for i, line in enumerate(lines):
        win, our = parse_line(line)
        w = len(win & our)
        for j in range(w):
            idx = i + j + 1
            if idx >= len(counts):
                break
            counts[idx] += counts[i]
    return sum(counts)


if __name__ == "__main__":
    data = read_file(f"samples/04.in")
    data = read_file(f"ins/04.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
