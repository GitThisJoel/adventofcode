import sys

sys.path.extend([".", ".."])

from utils import *

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

sample_vis = {
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (3, 3),
    (4, 3),
    (2, 4),
    (3, 4),
}


def print_knots(ps, dim=20):
    grid = [["." for _ in range(dim)] for _ in range(dim)]
    for i in range(len(ps)):
        x, y = ps[i]
        grid[-y + dim // 2][x + dim // 2] = str(i)
    for r in grid:
        print("".join(r))
    print("~~~~~~~~~~~~~~~~~~~~~~")


def dist(s, t):
    return max(abs(s[0] - t[0]), abs(s[1] - t[1]))


def steps(ph, pt):
    dx = ph[0] - pt[0]
    dy = ph[1] - pt[1]
    if abs(dx) == 2:
        dx = int((dx / abs(dx))) * (abs(dx) - 1)
    if abs(dy) == 2:
        dy = int((dy / abs(dy))) * (abs(dy) - 1)
    return dx, dy


def move_pt(ph, pt):
    if dist(ph, pt) <= 1:  # one step away, no need to move
        return pt
    dx, dy = steps(ph, pt)
    return [pt[0] + dx, pt[1] + dy]


def p1(data):
    ph = [0, 0]
    pt = [0, 0]
    vis = {tuple(pt)}

    lines = get_lines(data)
    for line in lines:
        d, s = line.split()
        dx, dy = dirs[d]
        for _ in range(int(s)):
            ph = [ph[0] + dx, ph[1] + dy]
            pt = move_pt(ph, pt)
            vis.add(tuple(pt))
    return len(vis)


def p2(data):
    knots = 10
    ps = [[0, 0] for _ in range(knots)]
    vis = {tuple(ps[-1])}

    lines = get_lines(data)
    for line in lines:
        d, s = line.split()
        dx, dy = dirs[d]
        for _ in range(int(s)):
            ps[0] = [ps[0][0] + dx, ps[0][1] + dy]

            for i in range(1, len(ps)):
                ps[i] = move_pt(ps[i - 1], ps[i])
            # print_knots(ps, dim=30)
            vis.add(tuple(ps[-1]))
    return len(vis)


if __name__ == "__main__":
    data = read_file(f"ins/09.in")
    # data = read_file(f"samples/09.in")
    # data = read_file(f"samples/09_2.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
