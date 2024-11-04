import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
"""


pipe_delta = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    ".": [(0, 0)],
}


def neighbours(x, y, board):
    ns = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= (x + dx) < len(board[0]) and 0 <= (y + dy) < len(board):
            ns.append((x + dx, y + dy))
    return ns


def s_pos(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "S":
                return j, i


def find_path(board, start):
    q = [start]
    path = [start]
    vis = set(q)
    found = False
    while len(q) > 0:
        px, py = q.pop()
        c = board[py][px]
        neighs = [(px + dx, py + dy) for dx, dy in pipe_delta[c]]
        for nx, ny in neighs:
            if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
                continue
            if board[ny][nx] == "S":
                found = True
            elif (nx, ny) not in vis:
                q.append((nx, ny))
                vis.add((nx, ny))
                path.append((nx, ny))
    return found, path


def find_area(path):
    # shoelace formula
    A = 0
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        A += (y2 - y1) * (x2 + x1)
    A = (abs(A) - len(path) + 2) // 2
    return A


def p1(data):
    board = get_lines(data)
    sx, sy = s_pos(board)
    for nx, ny in neighbours(sx, sy, board):
        found, path = find_path(board, (nx, ny))
        if found:
            break
    path.append((sx, sy))
    return len(path) // 2


def p2(data):
    board = get_lines(data)
    sx, sy = s_pos(board)
    for nx, ny in neighbours(sx, sy, board):
        found, path = find_path(board, (nx, ny))
        if found:
            break
    path.append((sx, sy))
    return find_area(path)


if __name__ == "__main__":
    # data = read_file("2023/samples/10.in")
    data = read_file("2023/ins/10.in")
    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
