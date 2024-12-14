import sys
from pprint import pprint
from scanf import scanf

sys.path.extend([".", ".."])

from utils import *


def calc_score(seconds, lines):
    R, C = 103, 101
    # R, C = 7, 11
    MR = R // 2
    MC = C // 2
    quads = [0] * 4
    for line in lines:
        x, y, dx, dy = scanf("p=%d,%d v=%d,%d", line)
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

    ans = 1
    for n in quads:
        ans *= n
    return ans


def p1(data):
    lines = get_lines(data)
    return calc_score(100, lines)


def p2(data):
    lines = get_lines(data)
    R, C = 103, 101
    min_score = calc_score(0, lines)
    for seconds in range(1, R * C):
        score = calc_score(seconds, lines)
        if score < min_score:
            min_score = score
            print(f"{seconds=}")
            B = [["." for _ in range(C)] for _ in range(R)]
            for line in lines:
                x, y, dx, dy = scanf("p=%d,%d v=%d,%d", line)
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
