import sys
from pprint import pprint
from tqdm import tqdm

sys.path.extend([".", ".."])

from utils import *


def read_monkeys(lines, human_shout=None):
    shouts, exprs = {}, {}
    for line in lines:
        m, a = line.split(": ")
        if a.isdigit():
            shouts[m] = int(a)
        else:
            exprs[m] = a
    if human_shout is not None:
        shouts["humn"] = human_shout
        exprs["root"] = exprs["root"].replace("+", "-")
    return shouts, exprs


def get_root(lines, human_shout=None):
    shouts, exprs = read_monkeys(lines, human_shout=human_shout)
    while "root" in exprs:
        remove_monkeys = set()
        for m, a in exprs.items():
            m1, op, m2 = a.split()
            if m1 in shouts and m2 in shouts:
                e = f"{shouts[m1]}{op}{shouts[m2]}"
                shouts[m] = int(eval(e))
                remove_monkeys.add(m)
        for m in remove_monkeys:
            del exprs[m]
    return shouts["root"]


def p1(data):
    return get_root(get_lines(data))


def p2(data):
    lines = get_lines(data)

    h0 = get_root(lines, 0)
    sig = int(h0 / abs(h0))  # otherwise optimization in wrong direction
    lo = 0
    hi = 10**20
    while lo < hi:
        mid = (hi + lo) // 2
        hm = get_root(lines, human_shout=mid)
        if sig * hm > 0:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    data = read_file(f"samples/21.in")
    data = read_file(f"ins/21.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
