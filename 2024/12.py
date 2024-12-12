import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def find_group(G, start, vis):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    L = G[start[0]][start[1]]
    R = len(G)
    C = len(G[0])

    Q = [start]
    group = {}
    while len(Q) > 0:
        v = Q.pop()
        if v in group:
            continue
        neighs = []
        i, j = v
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if (0 <= ni < R) and (0 <= nj < C):
                if G[ni][nj] != L:
                    continue
                neighs.append((ni, nj))
                Q.append((ni, nj))
        group[i, j] = neighs

    for v in group:
        vis.add(v)

    sides = 0
    perimeter = set()
    for k in group:
        i, j = k
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if (ni, nj) not in group:
                perimeter.add((i, j, ni, nj))
    for i, j, ni, nj in perimeter:
        if (i - 1, j, ni - 1, nj) in perimeter:
            continue
        if (i, j - 1, ni, nj - 1) in perimeter:
            continue
        sides += 1

    return len(group), sum(4 - len(n) for n in group.values()), sides, vis


def p1(data):
    G = get_lines(data)

    vis = set()
    ans = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if (i, j) in vis:
                continue
            area, perimiter, _, vis = find_group(G, (i, j), vis)
            ans += area * perimiter
    return ans


def p2(data):
    G = get_lines(data)

    vis = set()
    ans = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if (i, j) in vis:
                continue
            area, _, sides, vis = find_group(G, (i, j), vis)
            ans += area * sides
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/12.in")
    data = read_file(f"2024/ins/12.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
