from math import ceil

from utils.parsing import read_file


def parse(data: str) -> list[tuple[int, int]]:
    return [tuple(map(int, r.split("-"))) for r in data.split(",")]


def check_repeating(x: int, start: int) -> bool:
    sx = str(x)
    for i in range(start, len(sx) // 2 + 1):
        if len(sx) % i != 0:  # should use all numbers in 'x'
            continue
        ok = True
        s = sx[:i]
        for j in range(0, len(sx), i):
            if s != sx[j : j + i]:
                ok = False
                break
        if ok:
            return True
    return False


def p1(data: str) -> int:
    ranges = parse(data)

    ans = 0
    for a, b in ranges:
        for i in range(a, b + 1):
            start = max(1, ceil(len(str(i)) / 2))
            if check_repeating(i, start):
                ans += i
    return ans


def p2(data: str) -> int:
    ranges = parse(data)

    ans = 0
    for a, b in ranges:
        for i in range(a, b + 1):
            if check_repeating(i, 1):
                ans += i
    return ans


if __name__ == "__main__":
    data = read_file("2025/samples/02.in")
    data = read_file("2025/ins/02.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
