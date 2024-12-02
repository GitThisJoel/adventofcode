import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *


def create_diffs(line) -> list[int]:
    diffs = []
    for i in range(len(line) - 1):
        diffs.append(line[i] - line[i + 1])
    return diffs


def is_safe(diffs) -> bool:
    lt0 = list(x < 0 for x in diffs)
    gt0 = list(x > 0 for x in diffs)
    safe = all(0 < abs(x) < 4 for x in diffs) and (all(lt0) or all(gt0))
    return safe


def p1(data):
    lines = get_int_lines(data)

    ans = 0
    for line in lines:
        diffs = create_diffs(line)
        ans += 1 if is_safe(diffs) else 0
    return ans


def p2(data):
    lines = get_int_lines(data)

    ans = 0
    for line in lines:
        diffs = create_diffs(line)
        safe = is_safe(diffs)

        if not safe:
            for i in range(len(line)):
                diffs = create_diffs(line[:i] + line[i + 1 :])
                safe = safe or is_safe(diffs)
        ans += 1 if safe else 0
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/02.in")
    data = read_file(f"2024/ins/02.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
