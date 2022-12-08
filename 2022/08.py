import sys

sys.path.extend([".", ".."])

from utils import *


def visable(t, l):
    return t > max(l)


def score(t, l):
    r = []
    for n in l:
        r.append(n)
        if n >= t:
            break
    return len(r)


def read_forest(data):
    lines = get_lines(data)
    forest = list()
    for line in lines:
        forest.append([int(c) for c in line])
    return forest


def p1(data):
    forest = read_forest(data)

    vis = [
        [
            i == 0 or j == 0 or i == len(forest[0]) - 1 or j == len(forest) - 1
            for i in range(len(forest[0]))
        ]
        for j in range(len(forest))
    ]

    for x in range(1, len(forest[0]) - 1):
        for y in range(1, len(forest) - 1):
            t = forest[y][x]
            col = [forest[i][x] for i in range(len(forest))]

            r1 = forest[y][:x]
            r2 = forest[y][x + 1 :]
            r3 = col[:y]
            r4 = col[y + 1 :]

            vis[y][x] = (
                visable(t, r1) or visable(t, r2) or visable(t, r3) or visable(t, r4)
            )

    return sum(sum(vis, []))


def p2(data):
    forest = read_forest(data)

    hi = -1
    for x in range(1, len(forest[0]) - 1):
        for y in range(1, len(forest) - 1):
            t = forest[y][x]
            col = [forest[i][x] for i in range(len(forest))]

            r1 = forest[y][:x][::-1]
            r2 = forest[y][x + 1 :]
            r3 = col[:y][::-1]
            r4 = col[y + 1 :]
            s = score(t, r1) * score(t, r2) * score(t, r3) * score(t, r4)
            if s > hi:
                hi = s
    return hi


if __name__ == "__main__":
    data = read_file(f"ins/08.in")
    # data = read_file(f"samples/08.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
