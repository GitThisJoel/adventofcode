import sys

sys.path.extend([".", ".."])

from utils import *

from collections import defaultdict


def find_antennas(B):
    A = defaultdict(list)
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] != ".":
                A[B[i][j]].append((i, j))
    return [v for v in A.values()]


def p1(data):
    B = get_lines(data)
    A = find_antennas(B)

    antinodes = set()
    R = len(B)
    C = len(B[0])
    for poss in A:
        for i in range(len(poss) - 1):
            r1, c1 = poss[i]
            for j in range(i + 1, len(poss)):
                r2, c2 = poss[j]
                dr, dc = r1 - r2, c1 - c2
                a1 = r1 + dr, c1 + dc
                a2 = r2 - dr, c2 - dc
                for r, c in [a1, a2]:
                    if (0 <= r < R) and (0 <= c < C):
                        antinodes.add((r, c))
    return len(antinodes)


def p2(data):
    B = get_lines(data)
    A = find_antennas(B)

    antinodes = set()
    R = len(B)
    C = len(B[0])
    for poss in A:
        for i in range(len(poss) - 1):
            r1, c1 = poss[i]
            for j in range(i + 1, len(poss)):
                r2, c2 = poss[j]
                dr, dc = r1 - r2, c1 - c2

                # change "start" point from part 1 since the antennas
                # themself can be included as their own antinodes.
                r, c = r2 + dr, c2 + dc
                while (0 <= r < R) and (0 <= c < C):
                    antinodes.add((r, c))
                    r, c = r + dr, c + dc

                r, c = r1 - dr, c1 - dc
                while (0 <= r < R) and (0 <= c < C):
                    antinodes.add((r, c))
                    r, c = r - dr, c - dc
    return len(antinodes)


if __name__ == "__main__":
    data = read_file(f"2024/samples/08.in")
    data = read_file(f"2024/ins/08.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
