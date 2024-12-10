import sys

sys.path.extend([".", ".."])

from utils import *

from collections import defaultdict


def create_graph(data):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    G = defaultdict(set)
    zeroes = []
    R = len(data)
    C = len(data[0])
    for i in range(R):
        for j in range(C):
            v = data[i][j]
            if v == 0:
                zeroes.append((i, j))
            for di, dj in dirs:
                if not (0 <= i + di < R and 0 <= j + dj < C):
                    continue
                if data[i + di][j + dj] - v == 1:
                    G[i, j].add((i + di, j + dj))
    return dict(G), zeroes


def bfs(start, G, data, goal=9):
    Q = [start]
    vis = {start}
    total = 0
    goals = []
    while len(Q) > 0:
        v = Q.pop()
        if data[v[0]][v[1]] == goal:
            goals.append(v)
            total += 1
        for neigh in G.get(v, set()):
            if neigh in vis:
                continue
            vis.add(neigh)
            Q.append(neigh)
    return total, goals


def count_paths(zeroes, G, data, goal=9):
    dists = {}
    for k, w in G.items():
        dists[k] = 0
        for v in w:
            dists[v] = 0

    for zero in zeroes:
        dists[zero] = 1

    Q = zeroes
    while len(Q) > 0:
        v = Q.pop()
        for neigh in G.get(v, set()):
            dists[neigh] += 1
            Q.append(neigh)

    R = len(data)
    C = len(data[0])
    tot = 0
    for i in range(R):
        for j in range(C):
            if data[i][j] == goal:
                tot += dists.get((i, j), 0)
    return tot


def p1(data):
    G, zeroes = create_graph(data)
    ans = 0
    for zero in zeroes:
        t, _ = bfs(zero, G, data)
        ans += t
    return ans


def p2(data):
    G, zeroes = create_graph(data)
    return count_paths(zeroes, G, data, goal=9)


if __name__ == "__main__":
    data = read_file(f"2024/samples/10.in")
    data = read_file(f"2024/ins/10.in")

    # conv str -> int
    data = [[int(c) for c in line] for line in get_lines(data)]

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
