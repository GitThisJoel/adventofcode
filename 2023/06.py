import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def dist(hold, T):
    return hold * (T - hold)


def find_limit(T, D, dirr):
    lim = None
    hold = 0 if dirr > 0 else T
    while lim is None:
        d = dist(hold, T)
        if d > D:
            lim = hold
        hold += dirr
    return lim


def p1(data):
    lines = get_lines(data)
    tups = []
    for t in zip(*[line.split()[1:] for line in lines]):
        tups.append(tuple(map(int, t)))

    # sol 1
    ans = 1
    for T, D in tups:
        beats = 0
        for i in range(T + 1):
            d = dist(i, T)
            if d > D:
                beats += 1
        ans *= beats

    # sol 2
    ans = 1
    for T, D in tups:
        left = find_limit(T, D, 1)
        right = find_limit(T, D, -1)
        ans *= right - left + 1

    return ans


def p2(data):
    lines = get_lines(data)
    T = int("".join(lines[0].split()[1:]))
    D = int("".join(lines[1].split()[1:]))
    left = find_limit(T, D, 1)
    right = find_limit(T, D, -1)
    return right - left + 1


if __name__ == "__main__":
    data = read_file(f"samples/06.in")
    data = read_file(f"ins/06.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
