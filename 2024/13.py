import sys

sys.path.extend([".", ".."])

from utils import *


def parse(chunks, extra=0):
    CM = []
    for chunk in chunks:
        a = tuple(int(c.removeprefix("X+").removeprefix("Y+")) for c in chunk[0].split(": ")[1].split(", "))
        b = tuple(int(c.removeprefix("X+").removeprefix("Y+")) for c in chunk[1].split(": ")[1].split(", "))
        p = tuple(int(c.removeprefix("X=").removeprefix("Y=")) + extra for c in chunk[2].split(": ")[1].split(", "))
        CM.append([a, b, p])
    return CM


def find_presses(CM):
    ans = 0
    for cm in CM:
        (x1, y1), (x2, y2), (px, py) = cm
        d = x2 * y1 - y2 * x1
        pb = (px * y1 - py * x1) / d
        pa = (py * x2 - px * y2) / d

        if pa.is_integer() and pb.is_integer():
            ans += 3 * int(pa) + int(pb)
    return ans


def p1(data):
    chunks = get_chunks(data)
    CM = parse(chunks)
    return find_presses(CM)


def p2(data):
    chunks = get_chunks(data)
    CM = parse(chunks, extra=10_000_000_000_000)
    return find_presses(CM)


if __name__ == "__main__":
    """
    Given:
    P_a * x_1 + P_b * x_2 = A_x
    P_a * y_1 + P_b * y_2 = A_y

    Find P_a and P_b using x, y and A.
    """
    data = read_file(f"2024/samples/13.in")
    data = read_file(f"2024/ins/13.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
