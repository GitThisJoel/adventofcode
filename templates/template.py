import sys

sys.path.extend([".", ".."])

from utils import *

current_day = 1337


def p1(data):
    lines = get_lines(data)
    chunks = data.split("\n\n")

    return


def p2(data):
    return


if __name__ == "__main__":
    data = read_file(f"ins/{current_day}.in")

    print(f"part 1: {p1(data)}")
    # print(f"part 2: {p2(data)}")
