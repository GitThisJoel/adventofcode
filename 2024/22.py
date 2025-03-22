import sys

sys.path.extend([".", ".."])

from collections import defaultdict
from pprint import pprint

from utils import *


def new_secret(s, iters):
    """
    s0 = s

    s1 = ((s0 * 64) ^ s0) % 16777216

    s2 = (floor(s1 / 32) ^ s1) % 16777216

    s3 = ((s2 * 2048) ^ s2) % 16777216
    """
    m = 16777216
    for _ in range(iters):
        s = ((s << 6) ^ s) % m
        s = ((s >> 5) ^ s) % m
        s = ((s << 11) ^ s) % m
    return s


def p1(data):
    secret_numbers = get_ints(data)
    ans = 0
    for s in secret_numbers:
        ans += new_secret(s, 2000)
    return ans


def p2(data):
    secret_numbers = get_ints(data)
    prices = defaultdict(int)
    for s in secret_numbers:
        seen = set()
        prev_price = s % 10
        deltas = []

        # set up initial values
        for _ in range(3):
            s = new_secret(s, 1)
            p = s % 10
            deltas.append(p - prev_price)
            prev_price = p

        for _ in range(2000 - 3):
            s = new_secret(s, 1)
            p = s % 10
            deltas.append(p - prev_price)
            prev_price = p

            td = tuple(deltas)
            deltas.pop(0)
            if td in seen:  # only first occurence of sequence counts
                continue
            seen.add(td)
            prices[td] += p

    return max(prices.values())


if __name__ == "__main__":
    data = read_file(f"2024/samples/22.in")
    data = read_file(f"2024/ins/22.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
