import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def p1(data):
    lines = get_lines(data)
    chunks = get_chunks(data)

    ans = 0
    return 0


def p2(data):
    lines = get_lines(data)
    chunks = get_chunks(data)

    ans = 0
    return 0


if __name__ == "__main__":
    data = read_file(f"ins/1337.in")
    data = read_file(f"samples/1337.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
