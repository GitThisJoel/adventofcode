import sys

sys.path.extend([".", ".."])

from utils import *


def find_start(m, start):
    for i in range(len(m)):
        if start in m[i]:
            return i, m[i].index(start)


def get_neighbours(m, i, j, pf):
    ret = []
    u = ord(m[i][j])
    if m[i][j] == "S":
        u = ord("a")
    elif m[i][j] == "E":
        u = ord("z")

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in dirs:
        if not (len(m) > (i + di) >= 0 and len(m[i]) > (j + dj) >= 0):
            continue  # skip this iteration

        v = ord(m[i + di][j + dj])
        if m[i + di][j + dj] == "E":
            v = ord("z")
        elif m[i + di][j + dj] == "S":
            v = ord("a")

        if pf(v, u):
            ret.append((i + di, j + dj))
    return ret


def bfs(m, start_char, end_char, pf):
    start = find_start(m, start_char)
    vis = {start}
    parent = {}  # {child: parent}
    Q = [start]  # change if time is a problem
    while len(Q) > 0:
        y, x = Q.pop(0)
        if m[y][x] == end_char:
            end = (y, x)
            return start, end, parent
        ns = get_neighbours(m, y, x, pf)
        for n in ns:
            if n not in vis:
                vis.add(n)
                parent[n] = (y, x)
                Q.append(n)
    return None, None, None


def pf1(v, u):
    return v - u <= 1


def pf2(v, u):
    return u - v <= 1


def count_length(s, e, parent):
    if s is None:
        return None
    l = 0
    c = e
    while c != s:
        c = parent[c]
        l += 1
    return l


def p1(data):
    m = get_lines(data)
    s, e, parent = bfs(m, "S", "E", pf1)
    return count_length(s, e, parent)


def p2(data):
    m = get_lines(data)
    s, e, parent = bfs(m, "E", "a", pf2)
    return count_length(s, e, parent)


if __name__ == "__main__":
    data = read_file(f"ins/12.in")
    # data = read_file(f"samples/12.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
