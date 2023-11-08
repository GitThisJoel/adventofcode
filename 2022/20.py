import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

from itertools import cycle


def mix(data, mult=1, repreat=1):
    data = [(idx, value * mult) for idx, value in enumerate(data)]
    idx_value_queue = cycle(data[:])
    n = len(data) - 1
    for _ in range(len(data) * repreat):
        idx, value = next(idx_value_queue)
        i = data.index((idx, value))
        j = (i + value + n) % n
        data.remove((idx, value))
        data.insert(j, (idx, value))

    i0 = [i for i, (_, value) in enumerate(data) if value == 0][0]
    inds = [(i0 + x) % len(data) for x in [1000, 2000, 3000]]
    vals = [data[i][1] for i in inds]
    # print(f"{inds=}")
    # print(f"{vals=},")
    return sum(vals)


def p1(data):
    return mix(data, mult=1, repreat=1)


def p2(data):
    return mix(data, mult=811589153, repreat=10)


if __name__ == "__main__":
    data = read_file(f"samples/20.in")
    data = read_file(f"ins/20.in")

    print(f"part 1: {p1(get_ints(data))}")
    print(f"part 2: {p2(get_ints(data))}")
