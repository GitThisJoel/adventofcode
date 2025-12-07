from functools import cache

from utils.parsing import get_lines, read_file


# use cache to skip recalculating the answer
@cache
def solve(data: str) -> tuple[int, int]:
    lines = get_lines(data)
    beams = {}  # for p2
    for i, c in enumerate(lines[0]):
        if c == "S":
            beams[i] = 1
    splits = 0  # for p1
    for line in lines[1:]:
        for i in list(beams.keys()):
            if line[i] == "^":
                splits += 1
                v = beams.pop(i)
                if i + 1 < len(line):
                    beams[i + 1] = beams.get(i + 1, 0) + v
                if i - 1 >= 0:
                    beams[i - 1] = beams.get(i - 1, 0) + v
    return splits, sum(beams.values())


def p1(data: str) -> int:
    splits, _ = solve(data)
    return splits


def p2(data: str) -> int:
    _, n_paths = solve(data)
    return n_paths


if __name__ == "__main__":
    data = read_file("2025/samples/07.in")
    data = read_file("2025/ins/07.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
