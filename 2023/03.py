import sys

from collections import defaultdict
from pprint import pprint

sys.path.extend([".", ".."])

from utils import *

num_gear_neighbour = defaultdict(list)


def check_neighbours(data, y, x):
    char_neigbour = False
    gear_pos = None
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if 0 <= y + dy < len(data) and 0 <= x + dx < len(data[y]):
                p = data[y + dy][x + dx]
                char_neigbour |= p != "." and not p.isdigit()
                if p == "*":
                    gear_pos = (y + dy, x + dx)
    return char_neigbour, gear_pos


def p1(data):
    global num_gear_neighbour
    data = get_lines(data)
    ans = 0
    for i in range(len(data)):
        curr_num = ""
        has_char_neighbour = False
        curr_gear_pos = None
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                curr_num += data[i][j]
                char_neighbour, gear_pos = check_neighbours(data, i, j)
                has_char_neighbour |= char_neighbour
                curr_gear_pos = gear_pos if gear_pos is not None else curr_gear_pos
            else:
                if has_char_neighbour:
                    ans += int(curr_num)
                    num_gear_neighbour[curr_gear_pos].append(int(curr_num))
                curr_num = ""
                has_char_neighbour = False
                curr_gear_pos = None
        if has_char_neighbour:
            ans += int(curr_num)
            num_gear_neighbour[curr_gear_pos].append(int(curr_num))
    return ans


def p2(data):
    global num_gear_neighbour
    if len(num_gear_neighbour) == 0:
        raise Exception("Run part 1 first")

    data = get_lines(data)
    ans = 0
    for _, nums in num_gear_neighbour.items():
        if len(nums) == 2:
            ans += nums[0] * nums[1]
    return ans


if __name__ == "__main__":
    data = read_file(f"samples/03.in")
    data = read_file(f"ins/03.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
