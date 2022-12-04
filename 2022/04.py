import sys

sys.path.extend([".", ".."])

from utils import *


def p1(data):
    lines = get_lines(data)
    c = 0
    for line in lines:
        l, r = line.split(",")
        ll = list(map(int, l.split("-")))
        rr = list(map(int, r.split("-")))

        if (ll[0] <= rr[0] and ll[1] >= rr[1]) or (rr[0] <= ll[0] and rr[1] >= ll[1]):
            c += 1

    return c


def p2(data):
    lines = get_lines(data)
    c = 0
    for line in lines:
        l, r = line.split(",")
        ll = list(map(int, l.split("-")))
        rr = list(map(int, r.split("-")))
        # init naive solution
        # s = set(range(ll[0], ll[1] + 1)).intersection(set(range(rr[0], rr[1] + 1)))
        # if len(s) > 0:
        #     c += 1

        rinl = (ll[0] <= rr[0] <= ll[1]) or (ll[0] <= rr[1] <= ll[1])
        linr = (rr[0] <= ll[0] <= rr[1]) or (rr[0] <= ll[1] <= rr[1])
        if rinl or linr:
            c += 1

    return c


# ..xxxxx...
# xxx...yyyy
if __name__ == "__main__":
    data = read_file(f"ins/04.in")
    # data = read_file(f"samples/04.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
