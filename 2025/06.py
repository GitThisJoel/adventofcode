from functools import reduce

from utils.parsing import get_lines, read_file


def solve_worksheet(cols: list[list[int]], ops: list[str]) -> int:
    ans = 0
    for i, op in enumerate(ops):
        if op == "+":
            ans += sum(cols[i])
        elif op == "*":
            ans += reduce(lambda a, b: a * b, cols[i], 1)
    return ans


def col_to_ints(col: list[str]) -> list[int]:
    assert all(len(col[i]) == len(col[0]) for i in range(len(col)))
    ints = []
    for i in range(len(col[0])):
        n = int("".join(c[i] for c in col).strip())
        ints.append(n)
    return ints


def p1(data: str) -> int:
    lines = get_lines(data)
    n = len(lines[0].split())
    cols = [[] for _ in range(n)]
    for line in lines[:-1]:
        for i, v in enumerate(map(int, line.split())):
            cols[i].append(v)
    return solve_worksheet(cols, lines[-1].split())


def p2(data: str) -> int:
    lines = get_lines(data)
    # pad lines to be the same length
    m = max(len(line) for line in lines[:-1])
    for i in range(len(lines)):
        if len(lines[i]) < m:
            lines[i] += " " * (m - len(lines[i]))
    op_line = lines[-1]
    cols = []

    def handle_col(curr: int | None, prev: int) -> None:
        col = []
        for line in lines[:-1]:
            c = curr - 1 if curr is not None else None
            col.append(line[prev:c])
        cols.append(col_to_ints(col))

    i = 1
    ip = 0
    while i < len(op_line):
        if op_line[i] != " ":
            handle_col(i, ip)
            ip = i
        i += 1
    handle_col(None, ip)
    return solve_worksheet(cols, op_line.split())


if __name__ == "__main__":
    data = read_file("2025/samples/06.in")
    data = read_file("2025/ins/06.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
