import sys

sys.path.extend([".", ".."])

from utils import *


def p1(data):
    lines = get_lines(data)
    s = 0
    tot_cycles = 0
    x = 1

    for line in lines:
        inst = line.strip().split()

        if len(inst) == 1:  # noop
            cycles = 1
            inc = 0
        else:
            cycles = 2
            inc = int(inst[1])

        for _ in range(cycles):
            tot_cycles += 1
            if (tot_cycles - 20) % 40 == 0:
                s += x * tot_cycles
        x += inc
    return s


def p2(data):
    lines = get_lines(data)
    tot_cycles = 0
    rows = []
    x = 1
    curr_row = ""

    for line in lines:
        inst = line.strip().split()
        if len(inst) == 1:  # noop
            cycles = 1
            inc = 0
        else:
            cycles = 2
            inc = int(inst[1])

        for _ in range(cycles):
            tot_cycles += 1
            if x - 1 <= len(curr_row) <= x + 1:
                curr_row += "#"
            else:
                curr_row += "."
            if tot_cycles % 40 == 0:
                rows.append(curr_row)
                curr_row = ""
        x += inc
    return rows


if __name__ == "__main__":
    data = read_file(f"ins/10.in")
    # data = read_file(f"samples/10.in")

    print(f"part 1: {p1(data)}")
    out = "\n".join(p2(data))
    print(f"part 2: \n{out}")
