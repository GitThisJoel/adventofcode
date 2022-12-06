import sys

sys.path.extend([".", ".."])

from utils import *


def p1(data, l=4):
    datastream = get_lines(data)[0]
    for i in range(len(datastream) - l - 1):
        if len(set(datastream[i : i + l])) == l:
            return i + l
    return -1


def p2(data):
    return p1(data, l=14)


if __name__ == "__main__":
    data = read_file(f"ins/06.in")
    # data = read_file(f"samples/06.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
