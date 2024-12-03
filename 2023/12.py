import sys

sys.path.extend([".", ".."])

from utils import *


def parse_line(line: str):
    groups, counts = line.strip().split()
    return groups, list(map(int, counts.split(",")))


def solve(groups: str, counts: list[int]):
    DP = {}

    def next_is_check(i):
        return groups[i] == "#" if i < len(groups) else False

    def count_arrangements(g: int, c: int) -> int:
        state = (g, c)
        if state in DP:
            return DP[state]

        if c >= len(counts):
            if all(p != "#" for p in groups[g:]):
                return 1
            return 0

        if g >= len(groups):
            DP[state] = 0
            return DP[state]

        if groups[g] == ".":
            DP[state] = count_arrangements(g + 1, c)
        elif groups[g] == "?":
            # ? == .
            arrs = count_arrangements(g + 1, c)

            # ? == #
            count = counts[c]
            nic = next_is_check(g + count)
            if (g + count) <= len(groups) and all(p != "." for p in groups[g : g + count]) and not nic:
                arrs += count_arrangements(g + count + 1, c + 1)

            DP[state] = arrs
        else:
            count = counts[c]
            arrs = 0
            nic = next_is_check(g + count)
            if (g + count) <= len(groups) and all(p != "." for p in groups[g : g + count]) and not nic:
                arrs = count_arrangements(g + count + 1, c + 1)

            DP[state] = arrs

        return DP[state]

    return count_arrangements(0, 0)


def p1(data):
    lines = get_lines(data)

    ans = 0
    for line in lines:
        groups, counts = parse_line(line)
        ans += solve(groups, counts)
    return ans


def p2(data):
    lines = get_lines(data)

    ans = 0
    rep = 5
    for line in lines:
        groups, counts = parse_line(line)
        groups = "?".join([groups] * rep)
        counts = counts * rep
        ans += solve(groups, counts)
    return ans


if __name__ == "__main__":
    data = read_file(f"2023/samples/12.in")
    data = read_file(f"2023/ins/12.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
