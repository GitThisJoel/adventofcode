import sys

sys.path.extend([".", ".."])

from functools import cache
from pprint import pprint

from utils import *


@cache
def valid_design(towels, design) -> int:
    if design == "":
        return 1

    valid = 0
    for towel in towels:
        if len(towel) > len(design):
            continue
        if towel == design[: len(towel)]:
            valid += valid_design(towels, design[len(towel) :])
    return valid


def get_valid_counts(data):
    (towels_line,), designs = get_chunks(data)
    towels = tuple(towels_line.split(", "))

    counts = []
    for design in designs:
        v = valid_design(towels, design)
        counts.append(v)
    return counts


def p1(counts):
    return len(list(filter(lambda x: x > 0, counts)))


def p2(counts):
    return sum(counts)


if __name__ == "__main__":
    data = read_file(f"2024/samples/19.in")
    data = read_file(f"2024/ins/19.in")
    counts = get_valid_counts(data)

    print(f"part 1: {p1(counts)}")
    print(f"part 2: {p2(counts)}")
