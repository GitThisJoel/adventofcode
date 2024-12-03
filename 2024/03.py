import sys
import regex as re

sys.path.extend([".", ".."])
from utils import *

mul_pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
comb_patterns = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don\'t)\(\)"


def p1(data):
    lines = get_lines(data)

    ans = 0
    for line in lines:
        for x, y in re.findall(mul_pattern, line):
            ans += int(x) * int(y)
    return ans


def p2(data):
    lines = get_lines(data)

    ans = 0
    k = 1
    for line in lines:
        for x, y, do, dont in re.findall(comb_patterns, line):
            if len(do) > 0:
                k = 1
            elif len(dont) > 0:
                k = 0
            else:
                ans += int(x) * int(y) * k
    return ans


if __name__ == "__main__":
    data = read_file(f"2024/samples/03.in")
    data = read_file(f"2024/ins/03.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
