import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def parse_line(line):
    game, raw_groups = line.split(": ")
    lid = int(game.split()[-1])
    cubes = []
    for split_group in raw_groups.split(";"):
        group = {"red": 0, "green": 0, "blue": 0}
        for e in split_group.split(", "):
            snum, color = e.split()
            group[color] = int(snum)
        cubes.append(group)
    return lid, cubes


def p1(data):
    lines = get_lines(data)

    ans = 0
    maxc = {"red": 12, "green": 13, "blue": 14}
    for line in lines:
        lid, cubes = parse_line(line)
        ok = True
        for group in cubes:
            ok &= all(group[color] <= maxc[color] for color in group.keys())
        if ok:
            ans += lid
    return ans


def p2(data):
    lines = get_lines(data)
    ans = 0
    for line in lines:
        lid, cubes = parse_line(line)
        minc = {"red": 0, "green": 0, "blue": 0}
        for group in cubes:
            for color in group.keys():
                minc[color] = max(minc[color], group[color])
        ans += minc["red"] * minc["green"] * minc["blue"]
    return ans


if __name__ == "__main__":
    data = read_file(f"samples/02.in")
    data = read_file(f"ins/02.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
