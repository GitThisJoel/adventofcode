import sys

sys.path.extend([".", ".."])

from utils import *


def p1(data):
    board = get_lines(data)
    L = len(board)
    N = len(board[0])

    dirs = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            dirs.append((dy, dx))
    dirs.remove((0, 0))

    ans = 0
    for i in range(L):
        for j in range(N):
            if board[i][j] != "X":
                continue
            for dy, dx in dirs:
                s = "X"
                for k in range(1, 4):
                    y = i + dy * k
                    x = j + dx * k
                    if (0 <= y < L) and (0 <= x < N):
                        s += board[y][x]
                    else:
                        break
                if s == "XMAS":
                    ans += 1
    return ans


def p2(data):
    board = get_lines(data)
    L = len(board)
    N = len(board[0])

    dirs = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

    ans = 0
    for i in range(L):
        for j in range(N):
            if board[i][j] != "A":
                continue
            ok = True
            for ds in dirs:
                s = ""
                for dy, dx in ds:
                    y = i + dy
                    x = j + dx
                    if (0 <= y < L) and (0 <= x < N):
                        s += board[y][x]
                    else:
                        break
                if not (s == "MS" or s == "SM"):
                    ok = False
            ans += 1 if ok else 0
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/04.in")
    data = read_file(f"2024/ins/04.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
