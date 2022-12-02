import sys

sys.path.extend([".", ".."])

from utils import *

current_day = 2

rules = {"A": "r", "B": "p", "C": "s", "X": "r", "Y": "p", "Z": "s"}
score = {"r": 1, "p": 2, "s": 3}


def p1(data):
    lines = get_lines(data)
    s = 0
    for l in lines:
        o, m = l.strip().split()
        os = score[rules[o]]
        ms = score[rules[m]]
        if os == ms:  # draw
            s += 3
        elif (ms - os) % 3 == 1:  # win
            s += 6
        s += ms
    return s


def p2(data):
    diff = {"X": -1, "Y": 0, "Z": 1}  # lose, tie, win

    lines = get_lines(data)
    s = 0
    for l in lines:
        o, m = l.strip().split()
        ms = (score[rules[o]] + diff[m] - 1) % 3 + 1
        s += (diff[m] + 1) * 3 + ms
    return s


if __name__ == "__main__":
    data = read_file(f"ins/0{current_day}.in")
    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
