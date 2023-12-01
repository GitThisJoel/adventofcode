from cProfile import label
import sys
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_int(line):
    avail = []
    for i, ch in enumerate(line):
        if ch.isdigit():
            avail.append((i, eval(ch)))
    return avail


def find_str(line):
    global numbers
    avail = []
    for i in range(len(line)):
        for j, number in enumerate(numbers):
            if line[i : i + len(number)] == number:
                avail.append((i, j + 1))
    return avail


def p1(data):
    lines = get_lines(data)
    s = 0
    for line in lines:
        nums = find_int(line)
        first, last = min(nums), max(nums)
        s += first[1] * 10 + last[1]
    return s


def p2(data):
    lines = get_lines(data)
    s = 0
    for line in lines:
        nums = []
        for found in find_int(line) + find_str(line):
            if found is None or len(found) < 2:
                continue
            nums.append(found)
        first, last = min(nums), max(nums)
        s += first[1] * 10 + last[1]
    return s


if __name__ == "__main__":
    data = read_file(f"samples/01.in")
    data = read_file(f"ins/01.in")
    print(f"part 1: {p1(data)}")

    data = read_file(f"samples/01_2.in")
    data = read_file(f"ins/01.in")
    print(f"part 2: {p2(data)}")
