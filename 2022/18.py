import sys
from pprint import pprint
from collections import deque

sys.path.extend([".", ".."])

from utils import *


def get_neighbours(drop):
    dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    x, y, z = drop
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in dxyz]


def in_limit(drop, limits):
    return all(limits[i][0] <= drop[i] <= limits[i][1] for i in range(3))


def get_neighbours_in_limit(drop, limits):
    neighbours = []
    for neighbour in get_neighbours(drop):
        if in_limit(drop, limits):
            neighbours.append(neighbour)
    return neighbours


def count_neighbours(drop, room) -> int:
    tot = 0
    for x2, y2, z2 in get_neighbours(drop):
        if 0 <= x2 < len(room[0][0]) and 0 <= y2 < len(room[0]) and 0 <= z2 < len(room):
            tot += room[z2][y2][x2]
    return tot


# first sol
def _p1(drops):
    lim = 30
    room = [[[0 for _ in range(lim)] for _ in range(lim)] for _ in range(lim)]
    for x, y, z in drops:
        room[z][y][x] = 1
    area = 0
    for drop in drops:
        nn = count_neighbours(drop, room)
        area += 6 - nn
    return area


def create_limits(drops):
    lmax = [max(d[i] + 1 for d in drops) for i in range(3)]
    lmin = [min(d[i] - 1 for d in drops) for i in range(3)]
    return list(zip(lmin, lmax))


def p1(data):
    lines = get_lines(data)
    # drops = [eval(d) for d in ["1,1,1", "2,1,1"]]
    drops = set(eval(d) for d in lines)
    area = 0
    for drop in drops:
        for neigh in get_neighbours(drop):
            if neigh not in drops:
                area += 1
    return area


def p2(data):
    lines = get_lines(data)
    drops = set(eval(d) for d in lines)
    limits = create_limits(drops)

    area = 0
    visited = set()
    q = deque([(1, 1, 1)])
    while q:
        curr_drop = q.popleft()
        if curr_drop in drops:
            area += 1
            continue
        if curr_drop not in visited:
            visited.add(curr_drop)
            for neigh in get_neighbours_in_limit(curr_drop, limits):
                q.append(neigh)

    return area


if __name__ == "__main__":
    data = read_file(f"samples/18.in")
    data = read_file(f"ins/18.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
