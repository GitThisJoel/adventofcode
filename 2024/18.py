import sys

from tqdm import tqdm

sys.path.extend([".", ".."])

from pprint import pprint
from queue import Queue

from utils import *


def print_state(vis, corrupted, board_size):
    B = [["."] * (board_size + 1) for _ in range(board_size + 1)]
    for i, j in vis:
        B[i][j] = "O"
    for i, j in corrupted:
        B[i][j] = "#"
    print()
    for row in B:
        print("".join(row))
    print()


def bfs(corrupted, board_size):
    start = 0, 0
    goal = board_size, board_size
    q = Queue()
    q.put(start)
    vis = {start}
    parents = {}
    while not q.empty():
        i, j = q.get()
        if (i, j) == goal:
            break
        for di, dj in four_dirs:
            ni, nj = nij = i + di, j + dj
            if not (0 <= ni <= board_size and 0 <= nj <= board_size):
                continue
            if nij in vis or nij in corrupted:
                continue
            vis.add(nij)
            parents[nij] = (i, j)
            q.put(nij)
    return parents


def p1(data, board_size=70, kilobytes=1024):
    lines = get_lines(data)
    all_corrupted = list(tuple(map(int, pair.removeprefix("(").removesuffix(")").split(",")[::-1])) for pair in lines)
    corrupted = set(all_corrupted[:kilobytes])

    parents = bfs(corrupted, board_size)
    node = (board_size, board_size)
    path = [node]
    while node != (0, 0):
        node = parents[node]
        path.append(node)
    return len(set(path)) - 1  # one less than path length


def p2(data, board_size=70):
    lines = get_lines(data)
    all_corrupted = list(tuple(map(int, pair.removeprefix("(").removesuffix(")").split(",")[::-1])) for pair in lines)
    for kb in tqdm(range(len(all_corrupted)), leave=False):
        corrupted = set(all_corrupted[: kb + 1])
        parents = bfs(corrupted, board_size)
        if (board_size, board_size) not in parents:
            break
    return all_corrupted[kb][::-1]  # reverese since points is stores as (y,x) but output should be (x,y)


if __name__ == "__main__":
    data = read_file(f"2024/samples/18.in")
    data = read_file(f"2024/ins/18.in")
    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
