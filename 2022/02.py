import sys

sys.path.extend([".", ".."])

from utils import *

current_day = 2

rules = {"A": "r", "B": "p", "C": "s", "X": "r", "Y": "p", "Z": "s"}
score = {"r": 1, "p": 2, "s": 3}

round_score = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


def round1(o, m):
    global score
    global rules
    global round_score

    return round_score[o + m] + score[rules[m]]


def p1(data):
    lines = get_lines(data)
    score = 0
    for l in lines:
        o, m = l.strip().split()
        score += round1(o, m)
    return score


def lose(o):
    rules = {"A": "Z", "B": "X", "C": "Y"}
    return 0, rules[o]


def draw(o):
    rules = {"A": "X", "B": "Y", "C": "Z"}
    return 3, rules[o]


def win(o):
    rules = {"A": "Y", "B": "Z", "C": "X"}
    return 6, rules[o]


def round2(o, m):
    # X lose, Y draw, Z win
    global score
    global rules
    mrules = {"X": lose, "Y": draw, "Z": win}
    s, r = mrules[m](o)
    return s + score[rules[r]]


def p2(data):
    mrules = {"X": 0, "Y": 3, "Z": 6}
    lines = get_lines(data)
    score = 0
    for l in lines:
        o, m = l.strip().split()
        score += round2(o, m)
    return score


if __name__ == "__main__":
    data = read_file(f"ins/0{current_day}.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
