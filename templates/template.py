import sys

sys.path.extend([".", ".."])

from utils import *


def p1(data):
    lines = get_lines(data)
    chunks = get_chunks(data)

    return


def p2(data):
    return


if __name__ == "__main__":
    data = read_file(f"ins/1337.in")
    # data = read_file(f"samples/1337.in")

    print(f"part 1: {p1(data)}")
    # print(f"part 2: {p2(data)}")
