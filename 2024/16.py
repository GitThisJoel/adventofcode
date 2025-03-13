import sys

from collections import defaultdict
from pprint import pprint
from heapq import heappush, heappop

sys.path.extend([".", ".."])

from utils import *

inf = float("inf")


def find_start_end(B):
    start, end = (-1, -1), (-1, -1)
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] == "S":
                start = i, j
            if B[i][j] == "E":
                end = i, j
    return start, end


def walk_maze(B, start, end):
    si, sj = start
    q = [(0, si, sj, 0, 1)]
    vis = {(si, sj, 0, 1)}

    while len(q) > 0:  # or not end?
        cost, i, j, di, dj = heappop(q)
        vis.add((i, j, di, dj))
        if end == (i, j):
            break

        new_states = [
            (cost + 1, i + di, j + dj, di, dj),  # continue straight ahead
            (cost + 1000, i, j, dj, -di),  # turn clockwise: (r, c) --> (c, -r)
            (cost + 1000, i, j, -dj, di),  # turn counterclockwise: (r, c) --> (-c, r)
        ]
        for new_cost, ni, nj, ndi, ndj in new_states:
            if B[ni][nj] == "#":
                continue
            if (ni, nj, ndi, ndj) in vis:
                continue
            heappush(q, (new_cost, ni, nj, ndi, ndj))
    return cost


def walk_maze_with_backtrack(B, start, end):
    si, sj = start
    q = [(0, si, sj, 0, 1)]
    lowest_cost = defaultdict(lambda: inf)
    lowest_cost[(si, sj, 0, 1)] = 0  # state --> lowest score
    backtrack = defaultdict(set)  # backwards walk direction
    best_cost = inf
    end_states = set()

    while len(q) > 0:
        cost, i, j, di, dj = heappop(q)
        state = (i, j, di, dj)
        l_cost = lowest_cost[state]
        if l_cost > cost:
            lowest_cost[state] = cost
        if end == (i, j):
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add(state)

        new_states = [
            (cost + 1, i + di, j + dj, di, dj),  # continue straight ahead
            (cost + 1000, i, j, dj, -di),  # turn clockwise: (r, c) --> (c, -r)
            (cost + 1000, i, j, -dj, di),  # turn counterclockwise: (r, c) --> (-c, r)
        ]
        for new_cost, ni, nj, ndi, ndj in new_states:
            if B[ni][nj] == "#":
                continue
            n_state = (ni, nj, ndi, ndj)
            lowest = lowest_cost[n_state]
            if lowest < new_cost:
                continue
            if lowest > new_cost:
                lowest_cost[n_state] = new_cost
                backtrack[n_state] = set()
            backtrack[n_state].add(state)
            heappush(q, (new_cost, ni, nj, ndi, ndj))

    states = set()
    while len(end_states) > 0:
        state = end_states.pop()
        states.add(state)
        for p_states in backtrack[state]:
            if any(s is None for s in p_states):
                continue
            end_states.add(p_states)
            states.add(p_states)
    return len({(i, j) for i, j, _, _ in states})


def p1(data):
    B = get_lines(data)
    start, end = find_start_end(B)
    cost = walk_maze(B, start, end)
    return cost


def p2(data):
    B = get_lines(data)
    start, end = find_start_end(B)
    cost = walk_maze_with_backtrack(B, start, end)
    return cost


if __name__ == "__main__":
    data = read_file(f"2024/samples/16.in")
    data = read_file(f"2024/ins/16.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
