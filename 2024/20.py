import sys

sys.path.extend([".", ".."])

from utils import *


def find_start_end(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == "S":
                start = i, j
            if M[i][j] == "E":
                end = i, j
    return start, end


def calc_all_distances(M, start, end):
    r, c = len(M), len(M[0])
    q = {end}
    distances = {end: 0}
    parents = {}
    d = 1
    while True:
        if len(q) == 0:
            break
        new_q = set()
        for i, j in q:
            for di, dj in four_dirs:
                ni, nj = nij = i + di, j + dj
                if not (0 <= ni < r and 0 <= nj < c):
                    continue
                if (ni, nj) in distances:
                    continue
                if M[ni][nj] == "#":
                    continue
                distances[nij] = d
                new_q.add(nij)
                parents[(i, j)] = nij  # since walking from end to start
        d += 1
        q = new_q

    # find the best path from end to start
    best_path = [end]
    node = end
    while node != start:
        node = parents[node]
        best_path.append(node)
    assert best_path[-1] == start

    return distances, best_path[::-1]  # reverse since we want start to end


def all_cheats(M, distances, max_distance, start):
    r, c = len(M), len(M[0])
    vis = {start}
    reachable = {}
    q = {start}
    d = 1
    for d in range(1, max_distance + 1):
        if len(q) == 0:  # nothing more to cheat through
            break
        new_q = set()
        for i, j in q:
            for di, dj in four_dirs:
                ni, nj = nij = i + di, j + dj
                if not (0 <= ni < r and 0 <= nj < c):
                    continue
                if nij in vis:
                    continue
                if nij in distances and nij not in reachable:  # found a '.'
                    reachable[nij] = d
                new_q.add(nij)
        q = new_q
    return reachable


def cheat(M, distances, best_path, max_distance):
    saves = []
    for i, j in best_path[:-1]:  # do not care for end point
        reachable = all_cheats(M, distances, max_distance, (i, j))
        for rij, cheat_length in reachable.items():
            delta = distances[(i, j)] - distances[rij] - cheat_length
            if delta > 0:
                saves.append(delta)
    return saves


def p1(M, distances, best_path):
    saves = cheat(M, distances, best_path, 2)
    return len(list(filter(lambda x: x >= 100, saves)))


def p2(M, distances, best_path):
    saves = cheat(M, distances, best_path, 20)
    return len(list(filter(lambda x: x >= 100, saves)))


if __name__ == "__main__":
    data = read_file(f"2024/samples/20.in")
    data = read_file(f"2024/ins/20.in")

    # no need to recalc these for part 1 resp. 2
    M = get_lines(data)
    start, end = find_start_end(M)
    distances, best_path = calc_all_distances(M, start, end)

    print(f"part 1: {p1(M, distances, best_path)}")
    print(f"part 2: {p2(M, distances, best_path)}")
