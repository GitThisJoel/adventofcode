from utils.parsing import get_lines, read_file

MOD = 100


def solve(data: str, intermediate_zeros: bool) -> int:
    lines = get_lines(data)
    pos, ans = 50, 0
    for line in lines:
        d, n = line[0], int(line[1:])
        m = 1 if d == "R" else -1
        if intermediate_zeros:
            if m == 1 and pos + n > 99:
                ans += (pos + n) // MOD
            elif m == -1 and pos - n <= 0:
                # '+1' here because '//MOD' do not count the "first time" '0' when moving left
                ans += (n - pos) // MOD + (1 if pos != 0 else 0)
        pos = (pos + n * m) % MOD
        if not intermediate_zeros:
            ans += 1 if pos == 0 else 0
    return ans


def p1(data: str) -> int:
    return solve(data, intermediate_zeros=False)


def p2(data: str) -> int:
    return solve(data, intermediate_zeros=True)


if __name__ == "__main__":
    data = read_file("2025/samples/01.in")
    data = read_file("2025/ins/01.in")

    print(f"part 1: {p1(data)}")
    print(f"part 2: {p2(data)}")
