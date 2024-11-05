import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def transpose(M):
    MT = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return ["".join(row) for row in MT]


def void_rows_columns(U):
    def void(U):
        inds = []
        for i, line in enumerate(U):
            if "#" not in line:
                inds.append(i)
        return inds

    void_rows = void(U)
    void_columns = void(transpose(U))
    return void_rows, void_columns


def galaxy_positions(U):
    gals = []
    for i in range(len(U)):
        for j in range(len(U[0])):
            if U[i][j] == "#":
                gals.append((i, j))
    return gals


def add_void(galaxies, void_columns, void_rows, cost):
    vg = []
    for r, c in galaxies:
        nr = r
        nc = c
        for vr in void_rows:
            if r >= vr:
                nr += cost
        for vc in void_columns:
            if c >= vc:
                nc += cost
        vg.append((nr, nc))
    return vg


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def solve(U, cost):
    void_rows, void_columns = void_rows_columns(U)
    galaxies = galaxy_positions(U)
    galaxies = add_void(galaxies, void_columns, void_rows, cost)

    ans = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            ans += dist(galaxies[i], galaxies[j])
    return ans


def p1(data):
    U = get_lines(data)
    return solve(U, cost=1)


def p2(data):
    U = get_lines(data)
    return solve(U, cost=1_000_000 - 1)


if __name__ == "__main__":
    data = read_file(f"2023/ins/11.in")
    # data = read_file(f"2023/samples/11.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
