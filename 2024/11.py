import sys

sys.path.extend([".", ".."])

from utils import *


def blink_n(n: int, stones):
    M = {}

    def blink(blinks_left, stone):
        if blinks_left == 0:
            return 1

        state = (blinks_left, stone)
        if state in M:
            return M[blinks_left, stone]

        if stone == 0:
            M[state] = blink(blinks_left - 1, 1)
        elif len(str(stone)) % 2 == 0:
            sd = str(stone)
            l = int(sd[: len(sd) // 2])
            r = int(sd[len(sd) // 2 :])
            M[state] = blink(blinks_left - 1, l) + blink(blinks_left - 1, r)
        else:
            M[state] = blink(blinks_left - 1, stone * 2024)
        return M[state]

    tot = 0
    for stone in stones:
        tot += blink(n, stone)
    return tot


def p1(stones):
    return blink_n(25, stones)


def p2(stones):
    return blink_n(75, stones)


if __name__ == "__main__":
    data = read_file(f"2024/samples/11.in")
    data = read_file(f"2024/ins/11.in")

    stones = get_ints(data)
    print(f"part 1: {p1(stones)}")
    print(f"part 2: {p2(stones)}")
