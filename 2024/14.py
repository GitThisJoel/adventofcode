import sys
from pprint import pprint
from scanf import scanf

sys.path.extend([".", ".."])

from utils import *

R, C = 103, 101


def calc_score(seconds, int_lines):
    MR = R // 2
    MC = C // 2
    quads = [0] * 4
    for x, y, dx, dy in int_lines:
        x = (x + dx * seconds) % C
        y = (y + dy * seconds) % R
        if x < MC and y < MR:  # Q1
            quads[0] += 1
        elif x > MC and y < MR:  # Q2
            quads[1] += 1
        elif x < MC and y > MR:  # Q3
            quads[2] += 1
        elif x > MC and y > MR:  # Q4
            quads[3] += 1

    score = 1
    for n in quads:
        score *= n
    return score


def p1(data):
    lines = get_lines(data)
    int_lines = [scanf("p=%d,%d v=%d,%d", line) for line in lines]
    return calc_score(100, int_lines)


def p2(data):
    lines = get_lines(data)
    int_lines = [scanf("p=%d,%d v=%d,%d", line) for line in lines]
    min_score = calc_score(0, int_lines)
    for seconds in range(1, R * C):
        score = calc_score(seconds, int_lines)
        if score < min_score:
            min_score = score
            print(f"{seconds=}")
            B = [["." for _ in range(C)] for _ in range(R)]
            for x, y, dx, dy in int_lines:
                x = (x + dx * seconds) % C
                y = (y + dy * seconds) % R
                B[y][x] = "*"
            pprint(["".join(b) for b in B])
            ans = input("continue? (y/n)")
            if "n" in ans:
                break
            print()
    return seconds


if __name__ == "__main__":
    data = read_file(f"2024/samples/14.in")
    data = read_file(f"2024/ins/14.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
