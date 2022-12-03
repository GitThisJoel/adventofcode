import sys

sys.path.extend([".", ".."])

from utils import *


def prio_score(c):
    if c.isupper():
        return ord(c) - ord("A") + 27
    else:
        return ord(c) - ord("a") + 1


def p1(data):
    s = 0
    lines = get_lines(data)
    for line in lines:
        com = set(line[: len(line) // 2]).intersection(set(line[len(line) // 2 :]))
        i = com.pop()
        s += prio_score(i)
    return s


def p2(data):
    s = 0
    lines = get_lines(data)
    for i in range(0, len(lines) - 2, 3):
        ss = [set(items) for items in lines[i : i + 3]]
        i = ss[0].intersection(ss[1]).intersection(ss[2]).pop()
        s += prio_score(i)
    return s


if __name__ == "__main__":
    data = read_file(f"ins/03.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
