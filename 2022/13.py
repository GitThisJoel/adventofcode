import sys

sys.path.extend([".", ".."])

from utils import *

#
def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r  # l > r, right order => neg
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)

    # else list list
    ll = len(l)
    lr = len(r)

    for li, ri in zip(l, r):
        v = compare(li, ri)
        if v != 0:  # 0 means equal val, comp next
            return v
    return ll - lr  # right order => neg


def p1(data):
    chunks = get_chunks(data)
    s = 0
    for i, chunk in enumerate(chunks):
        l = eval(chunk[0])
        r = eval(chunk[1])
        if compare(l, r) < 0:
            s += i + 1
    return s


def flatten(xs):
    ret = []
    while len(xs) > 0:
        elem = xs.pop(0)
        if type(elem) == int:
            ret.append(elem)
        else:
            ret += flatten(elem)
    return ret


def list_str(xs):
    return "".join(map(str, xs))


def p2(data):
    chunks = get_chunks(data)
    divs = [[[2]], [[6]]]
    cs = []
    for l, r in chunks:
        cs.append(eval(l))
        cs.append(eval(r))
    l1, l2 = 1, 2
    for c in cs:
        if compare(c, divs[0]) < 0:  # right order
            l1 += 1
        if compare(c, divs[1]) < 0:
            l2 += 1
    return l1 * l2


if __name__ == "__main__":
    data = read_file(f"ins/13.in")
    # data = read_file(f"samples/13.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
